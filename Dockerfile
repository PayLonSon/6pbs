# 使用 Python 3.11 的 slim 版本
FROM python:3.11-slim

# 避免產生 pyc 檔，並設定 Python 不做緩衝輸出
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 設定工作目錄
WORKDIR /code

# 複製 requirements.txt 並安裝套件
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 複製所有專案檔案到容器中
COPY . /code/

# 開放 8000 port
EXPOSE 8000

# 啟動 Django 開發伺服器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
