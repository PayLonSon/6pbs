# 針對物資進出記錄的軟刪除與修改追蹤方案

### 軟刪除進貨交易記錄

```sql
-- 開始事務處理
BEGIN TRANSACTION;

-- 1. 獲取要取消的交易記錄
DECLARE @ItemId INT, @Quantity DECIMAL(10,2);
SELECT @ItemId = ItemId, @Quantity = Quantity 
FROM Transactions 
WHERE TransactionId = @TransactionId AND IsDeleted = 0;

-- 2. 標記交易為已刪除
UPDATE Transactions
SET IsDeleted = 1,
    DeletedAt = GETDATE(),
    DeletedBy = @OperatorId,
    ModificationReason = @Reason
WHERE TransactionId = @TransactionId;

-- 3. 反向調整庫存數量 (如果是進貨交易，取消後需要減少庫存)
UPDATE Inventory
SET CurrentQuantity = CurrentQuantity - @Quantity,
    LastUpdatedAt = GETDATE()
WHERE ItemId = @ItemId;

-- 4. 記錄稽核日誌
INSERT INTO TransactionAuditLog 
(TransactionId, TransactionType, Action, OperatorId, ActionTime, Reason)
VALUES 
(@TransactionId, 'IN', 'CANCEL', @OperatorId, GETDATE(), @Reason);

COMMIT TRANSACTION;
```

### 軟刪除出庫/消耗交易記錄

```sql
-- 開始事務處理
BEGIN TRANSACTION;

-- 1. 獲取要取消的交易記錄
DECLARE @ItemId INT, @Quantity DECIMAL(10,2);
SELECT @ItemId = ItemId, @Quantity = Quantity 
FROM ConsumptionTransactions 
WHERE TransactionId = @TransactionId AND IsDeleted = 0;

-- 2. 標記交易為已刪除
UPDATE ConsumptionTransactions
SET IsDeleted = 1,
    DeletedAt = GETDATE(),
    DeletedBy = @OperatorId,
    ModificationReason = @Reason
WHERE TransactionId = @TransactionId;

-- 3. 反向調整庫存數量 (如果是出庫/消耗交易，取消後需要增加庫存)
UPDATE Inventory
SET CurrentQuantity = CurrentQuantity + @Quantity,
    LastUpdatedAt = GETDATE()
WHERE ItemId = @ItemId;

-- 4. 記錄稽核日誌
INSERT INTO TransactionAuditLog 
(TransactionId, TransactionType, Action, OperatorId, ActionTime, Reason)
VALUES 
(@TransactionId, 'CONSUMPTION', 'CANCEL', @OperatorId, GETDATE(), @Reason);

COMMIT TRANSACTION;
```

## 4. 實作交易記錄修改

### 修改進貨數量

```sql
-- 開始事務處理
BEGIN TRANSACTION;

-- 1. 獲取原始交易記錄
DECLARE @ItemId INT, @OldQuantity DECIMAL(10,2);
SELECT @ItemId = ItemId, @OldQuantity = Quantity 
FROM Transactions 
WHERE TransactionId = @TransactionId AND IsDeleted = 0;

-- 2. 調整庫存數量（計算差額並調整）
DECLARE @QuantityDifference DECIMAL(10,2) = @NewQuantity - @OldQuantity;

UPDATE Inventory
SET CurrentQuantity = CurrentQuantity + @QuantityDifference,
    LastUpdatedAt = GETDATE()
WHERE ItemId = @ItemId;

-- 3. 更新交易記錄
UPDATE Transactions
SET Quantity = @NewQuantity,
    IsModified = 1,
    ModificationReason = @Reason
WHERE TransactionId = @TransactionId;

-- 4. 記錄稽核日誌
INSERT INTO TransactionAuditLog 
(TransactionId, TransactionType, Action, OperatorId, ActionTime, FieldName, OldValue, NewValue, Reason)
VALUES 
(@TransactionId, 'IN', 'MODIFY', @OperatorId, GETDATE(), 'Quantity', 
 CAST(@OldQuantity AS VARCHAR), CAST(@NewQuantity AS VARCHAR), @Reason);

COMMIT TRANSACTION;
```

## 5. 建立檢視以方便查詢

### 交易修改歷史檢視

```sql
CREATE VIEW vw_TransactionModificationHistory AS
SELECT 
    tal.AuditId,
    tal.TransactionId,
    tal.TransactionType,
    tal.Action,
    CASE 
        WHEN tal.TransactionType = 'IN' THEN t.ItemId
        ELSE ct.ItemId
    END AS ItemId,
    i.ItemName,
    tal.ActionTime,
    tal.FieldName,
    tal.OldValue,
    tal.NewValue,
    s.Name AS OperatorName,
    tal.Reason
FROM TransactionAuditLog tal
LEFT JOIN Transactions t ON tal.TransactionId = t.TransactionId AND tal.TransactionType = 'IN'
LEFT JOIN ConsumptionTransactions ct ON tal.TransactionId = ct.TransactionId AND tal.TransactionType = 'CONSUMPTION'
JOIN Staff s ON tal.OperatorId = s.StaffId
LEFT JOIN Items i ON 
    CASE 
        WHEN tal.TransactionType = 'IN' THEN t.ItemId
        ELSE ct.ItemId
    END = i.ItemId
ORDER BY tal.ActionTime DESC;
```

### 已刪除交易檢視

```sql
CREATE VIEW vw_CancelledTransactions AS
SELECT 
    t.TransactionId,
    'IN' AS TransactionType,
    t.BatchId,
    t.ItemId,
    i.ItemName,
    t.Quantity,
    t.StandardUnit,
    t.TransactionDate,
    s1.Name AS OperatorName,
    t.SupplierId,
    sup.SupplierName,
    t.DeletedAt,
    s2.Name AS DeletedByName,
    t.ModificationReason
FROM Transactions t
JOIN Items i ON t.ItemId = i.ItemId
JOIN Staff s1 ON t.OperatorId = s1.StaffId
JOIN Staff s2 ON t.DeletedBy = s2.StaffId
LEFT JOIN Supplier sup ON t.SupplierId = sup.SupplierId
WHERE t.IsDeleted = 1

UNION ALL

SELECT 
    ct.TransactionId,
    'CONSUMPTION' AS TransactionType,
    ct.BatchId,
    ct.ItemId,
    i.ItemName,
    ct.Quantity,
    ct.StandardUnit,
    ct.TransactionDate,
    s1.Name AS OperatorName,
    NULL AS SupplierId,
    NULL AS SupplierName,
    ct.DeletedAt,
    s2.Name AS DeletedByName,
    ct.ModificationReason
FROM ConsumptionTransactions ct
JOIN Items i ON ct.ItemId = i.ItemId
JOIN Staff s1 ON ct.OperatorId = s1.StaffId
JOIN Staff s2 ON ct.DeletedBy = s2.StaffId
WHERE ct.IsDeleted = 1
ORDER BY DeletedAt DESC;
```

# 以批次ID查詢被修改的交易記錄

批次ID（BatchId）是連結相關交易的重要識別碼，您可以通過以下方式查詢特定批次中被修改的交易記錄：

## 1. 創建批次修改查詢視圖

```sql
CREATE VIEW vw_BatchModifiedTransactions AS
SELECT 
    'IN' AS TransactionType,
    t.TransactionId,
    t.BatchId,
    t.ItemId,
    i.ItemName,
    t.Quantity,
    t.StandardUnit,
    t.TransactionDate,
    s.Name AS OperatorName,
    t.SupplierId,
    sup.SupplierName,
    t.ModificationReason,
    (SELECT COUNT(*) FROM TransactionAuditLog 
     WHERE TransactionId = t.TransactionId AND TransactionType = 'IN') AS ModificationCount
FROM Transactions t
JOIN Items i ON t.ItemId = i.ItemId
JOIN Staff s ON t.OperatorId = s.StaffId
LEFT JOIN Supplier sup ON t.SupplierId = sup.SupplierId
WHERE t.IsModified = 1 AND t.IsDeleted = 0

UNION ALL

SELECT 
    'CONSUMPTION' AS TransactionType,
    ct.TransactionId,
    ct.BatchId,
    ct.ItemId,
    i.ItemName,
    ct.Quantity,
    ct.StandardUnit,
    ct.TransactionDate,
    s.Name AS OperatorName,
    NULL AS SupplierId,
    NULL AS SupplierName,
    ct.ModificationReason,
    (SELECT COUNT(*) FROM TransactionAuditLog 
     WHERE TransactionId = ct.TransactionId AND TransactionType = 'CONSUMPTION') AS ModificationCount
FROM ConsumptionTransactions ct
JOIN Items i ON ct.ItemId = i.ItemId
JOIN Staff s ON ct.OperatorId = s.StaffId
WHERE ct.IsModified = 1 AND ct.IsDeleted = 0;
```

## 2. 根據批次ID查詢修改過的交易

```sql
-- 基本查詢：根據批次ID查詢所有修改過的交易
SELECT * FROM vw_BatchModifiedTransactions
WHERE BatchId = @BatchId
ORDER BY TransactionDate DESC;
```

## 3. 創建批次修改歷史存儲過程

```sql
CREATE PROCEDURE GetBatchModificationHistory
    @BatchId VARCHAR(50)
AS
BEGIN
    -- 先顯示批次中所有被修改的交易記錄
    SELECT * FROM vw_BatchModifiedTransactions
    WHERE BatchId = @BatchId
    ORDER BY TransactionDate DESC;
    
    -- 再查詢這些交易的修改歷史
    SELECT 
        tal.TransactionId,
        tal.TransactionType,
        tal.Action,
        tal.ActionTime,
        tal.FieldName,
        tal.OldValue,
        tal.NewValue,
        s.Name AS ModifiedByName,
        tal.Reason,
        CASE 
            WHEN tal.TransactionType = 'IN' THEN t.BatchId
            ELSE ct.BatchId
        END AS BatchId
    FROM TransactionAuditLog tal
    LEFT JOIN Transactions t ON tal.TransactionId = t.TransactionId AND tal.TransactionType = 'IN'
    LEFT JOIN ConsumptionTransactions ct ON tal.TransactionId = ct.TransactionId AND tal.TransactionType = 'CONSUMPTION'
    JOIN Staff s ON tal.OperatorId = s.StaffId
    WHERE (t.BatchId = @BatchId OR ct.BatchId = @BatchId)
    ORDER BY tal.ActionTime DESC;
END
```

## 4. 批次修改摘要查詢

```sql
-- 查詢特定批次的修改摘要
SELECT 
    BatchId,
    COUNT(DISTINCT TransactionId) AS ModifiedTransactionsCount,
    SUM(ModificationCount) AS TotalModificationsCount,
    MAX(TransactionDate) AS LastTransactionDate,
    STRING_AGG(CONVERT(NVARCHAR(MAX), ItemName), ', ') AS ModifiedItems
FROM vw_BatchModifiedTransactions
WHERE BatchId = @BatchId
GROUP BY BatchId;
```

## 5. 查詢最常被修改的批次

```sql
-- 找出修改次數最多的批次
SELECT TOP 10
    BatchId,
    COUNT(DISTINCT TransactionId) AS ModifiedTransactionsCount,
    SUM(ModificationCount) AS TotalModificationsCount
FROM vw_BatchModifiedTransactions
GROUP BY BatchId
ORDER BY TotalModificationsCount DESC;
```

## 6. 使用範例

```sql
-- 查詢特定批次的所有修改過的交易
EXEC GetBatchModificationHistory 'BATCH-2025-03-001';

-- 簡單查詢
SELECT * FROM vw_BatchModifiedTransactions WHERE BatchId = 'BATCH-2025-03-001';
```

這些查詢和視圖可以幫助您全面了解特定批次中所有被修改的交易記錄，包括修改的詳細歷史，對於審計和問題追蹤非常有幫助。