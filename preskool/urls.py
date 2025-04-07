"""
URL configuration for preskool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app_6pbs import views as app_views
from dashboard_6pbs import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main
    path('index', dashboard_views.index, name='index'),
    path('teacher-dashboard', dashboard_views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard', dashboard_views.student_dashboard, name='student_dashboard'),
    path('parent-dashboard', dashboard_views.parent_dashboard, name='parent_dashboard'),

    # Authentication

    path('', app_views.login, name='login'),
    path('login-2', app_views.login_two, name='login_2'),
    path('login-3', app_views.login_three, name='login_3'),
    path('register', app_views.register, name='register'),
    path('register-2', app_views.register_two, name='register_2'),
    path('register-3', app_views.register_three, name='register_3'),
    path('forgot-password', app_views.forgot_password, name='forgot_password'),    
    path('forgot-password-2', app_views.forgot_password_two, name='forgot_password_2'),    
    path('forgot-password-3', app_views.forgot_password_three, name='forgot_password_3'),    
    path('reset-password', app_views.reset_password, name='reset_password'),  
    path('reset-password-2', app_views.reset_password_two, name='reset_password_2'),  
    path('reset-password-3', app_views.reset_password_three, name='reset_password_3'),  
    path('reset-password-success', app_views.reset_password_success, name='reset_password_success'),  
    path('reset-password-success-2', app_views.reset_password_success_two, name='reset_password_success_2'),  
    path('reset-password-success-3', app_views.reset_password_success_three, name='reset_password_success_3'),  
    path('email-verification', app_views.email_verification, name='email_verification'),  
    path('email-verification-2', app_views.email_verification_two, name='email_verification_2'),  
    path('email-verification-3', app_views.email_verification_three, name='email_verification_3'),  
    path('two-step-verification', app_views.two_step_verification, name='two_step_verification'),  
    path('two-step-verification-2', app_views.two_step_verification_two, name='two_step_verification_2'),  
    path('two-step-verification-3', app_views.two_step_verification_three, name='two_step_verification_3'),
    
    #Peoples
    
    path('student-grid', app_views.student_grid, name='student_grid'),
    path('student-list', app_views.student_list, name='student_list'),
    path('student-details', app_views.student_details, name='student_details'),
    path('student-time-table', app_views.student_time_table, name='student_time_table'),
    path('student-leaves', app_views.student_leaves, name='student_leaves'),
    path('student-fees', app_views.student_fees, name='student_fees'),
    path('student-result', app_views.student_result, name='student_result'),
    path('student-library', app_views.student_library, name='student_library'),
    path('student-promotion', app_views.student_promotion, name='student_promotion'),
    path('add-student', app_views.add_student, name='add_student'),
    path('edit-student', app_views.edit_student, name='edit_student'),
    
    path('parent-grid', app_views.parent_grid, name='parent_grid'),
    path('parent-list', app_views.parent_list, name='parent_list'),    
    path('guardian-grid', app_views.guardian_grid, name='guardian_grid'),
    path('guardian-list', app_views.guardian_list, name='guardian_list'),
    
    path('teacher-grid', app_views.teacher_grid, name='teacher_grid'),   
    path('teacher-list', app_views.teacher_list, name='teacher_list'),   
    path('add-teacher', app_views.add_teacher, name='add_teacher'),   
    path('edit-teacher', app_views.edit_teacher, name='edit_teacher'),   
    path('teacher-details', app_views.teacher_details, name='teacher_details'),   
    path('routine-teachers', app_views.routine_teachers, name='routine_teachers'),   
    path('teacher-leaves', app_views.teacher_leaves, name='teacher_leaves'),   
    path('teacher-salary', app_views.teacher_salary, name='teacher_salary'),   
    path('teacher-library', app_views.teacher_library, name='teacher_library'),   
    
    # Application
    
    path('chat', app_views.chat, name='chat'), 
    path('call', app_views.call, name='call'), 
    path('calendar', app_views.calendar, name='calendar'), 
    path('email', app_views.email, name='email'), 
    path('todo', app_views.todo, name='todo'), 
    path('notes', app_views.notes, name='notes'), 
    path('file-manager', app_views.file_manager, name='file_manager'), 
    path('video-call', app_views.video_call, name='video_call'), 
    
    #Content
    
    path('pages', app_views.pages, name="pages"),
    path('testimonials', app_views.testimonials, name="testimonials"),
    path('faq', app_views.faq, name="faq"),
    
    path('blog', app_views.blog, name="blog"),
    path('blog-categories', app_views.blog_categories, name="blog_categories"),
    path('blog-comments', app_views.blog_comments, name="blog_comments"),
    path('blog-tags', app_views.blog_tags, name="blog_tags"),
        
    path('countries', app_views.countries, name="countries"),
    path('states', app_views.states, name="states"),
    path('cities', app_views.cities, name="cities"),
    
    #Settings
    
    path('profile-settings', app_views.profile_settings, name='profile_settings'), 
    path('security-settings', app_views.security_settings, name='security_settings'), 
    path('notifications-settings', app_views.notifications_settings, name='notifications_settings'), 
    path('connected-apps', app_views.connected_apps, name='connected_apps'), 
    
    path('company-settings', app_views.company_settings, name='company_settings'),    
    path('localization', app_views.localization, name='localization'),    
    path('prefixes', app_views.prefixes, name='prefixes'),    
    path('social-authentication', app_views.social_authentication, name='social_authentication'),    
    path('preferences', app_views.preferences, name='preferences'),    
    path('language', app_views.language, name='language'), 
       
    path('invoice-settings', app_views.invoice_settings, name='invoice_settings'),    
    path('custom-fields', app_views.custom_fields, name='custom_fields'),    
    
    path('email-settings', app_views.email_settings, name='email_settings'),    
    path('email-templates', app_views.email_templates, name='email_templates'),    
    path('sms-settings', app_views.sms_settings, name='sms_settings'),    
    path('otp-settings', app_views.otp_settings, name='otp_settings'),    
    path('gdpr-cookies', app_views.gdpr_cookies, name='gdpr_cookies'), 
       
    path('payment-gateways', app_views.payment_gateways, name='payment_gateways'),    
    path('tax-rates', app_views.tax_rates, name='tax_rates'),    
    
    path('school-settings', app_views.school_settings, name='school_settings'),    
    path('religion', app_views.religion, name='religion'),   
     
    path('storage', app_views.storage, name='storage'),    
    path('ban-ip-address', app_views.ban_ip_address, name='ban_ip_address'),    

    #Management
    
    path('fees-group', app_views.fees_group, name='fees_group'),    
    path('fees-type', app_views.fees_type, name='fees_type'),    
    path('fees-master', app_views.fees_master, name='fees_master'),    
    path('fees-assign', app_views.fees_assign, name='fees_assign'),    
    path('collect-fees', app_views.collect_fees, name='collect_fees'),  
    
    path('library-members', app_views.library_members, name='library_members'), 
    path('library-books', app_views.library_books, name='library_books'), 
    path('library-issue-book', app_views.library_issue_book, name='library_issue_book'), 
    path('library-return', app_views.library_return, name='library_return'), 
    
    
    path('sports', app_views.sports, name='sports'), 
    path('players', app_views.players, name='players'), 
    
    path('hostel-list', app_views.hostel_list, name='hostel_list'), 
    path('hostel-rooms', app_views.hostel_rooms, name='hostel_rooms'), 
    path('hostel-room-type', app_views.hostel_room_type, name='hostel_room_type'), 
    
    path('transport-routes', app_views.transport_routes, name='transport_routes'), 
    path('transport-pickup-points', app_views.transport_pickup_points, name='transport_pickup_points'), 
    path('transport-vehicle-drivers', app_views.transport_vehicle_drivers, name='transport_vehicle_drivers'), 
    path('transport-vehicle', app_views.transport_vehicle, name='transport_vehicle'), 
    path('transport-assign-vehicle', app_views.transport_assign_vehicle, name='transport_assign_vehicle'), 
    
    #UI Module
    
    path('ui-alerts', app_views.ui_alerts, name='ui_alerts'),
    path('ui-accordion', app_views.ui_accordion, name='ui_accordion'),
    path('ui-avatar', app_views.ui_avatar, name='ui_avatar'),
    path('ui-badges', app_views.ui_badges, name='ui_badges'),
    path('ui-borders', app_views.ui_borders, name='ui_borders'),
    path('ui-buttons', app_views.ui_buttons, name='ui_buttons'),
    path('ui-buttons-group', app_views.ui_buttons_group, name='ui_buttons_group'),
    path('ui-breadcrumb', app_views.ui_breadcrumb, name='ui_breadcrumb'),
    path('ui-cards', app_views.ui_cards, name='ui_cards'),
    path('ui-carousel', app_views.ui_carousel, name='ui_carousel'),
    path('ui-colors', app_views.ui_colors, name='ui_colors'),
    path('ui-dropdowns', app_views.ui_dropdowns, name='ui_dropdowns'),
    path('ui-grid', app_views.ui_grid, name='ui_grid'),
    path('ui-images', app_views.ui_images, name='ui_images'),
    path('ui-lightbox', app_views.ui_lightbox, name='ui_lightbox'),
    path('ui-media', app_views.ui_media, name='ui_media'),
    path('ui-modals', app_views.ui_modals, name='ui_modals'),
    path('ui-offcanvas', app_views.ui_offcanvas, name='ui_offcanvas'),
    path('ui-pagination', app_views.ui_pagination, name='ui_pagination'),
    path('ui-popovers', app_views.ui_popovers, name='ui_popovers'),
    path('ui-progress', app_views.ui_progress, name='ui_progress'),
    path('ui-placeholders', app_views.ui_placeholders, name='ui_placeholders'),
    path('ui-spinner', app_views.ui_spinner, name='ui_spinner'),
    path('ui-sweetalerts', app_views.ui_sweetalerts, name='ui_sweetalerts'),
    path('ui-nav-tabs', app_views.ui_nav_tabs, name='ui_nav_tabs'),
    path('ui-toasts', app_views.ui_toasts, name='ui_toasts'),
    path('ui-tooltips', app_views.ui_tooltips, name='ui_tooltips'),
    path('ui-typography', app_views.ui_typography, name='ui_typography'),
    path('ui-video', app_views.ui_video, name='ui_video'),
        
    # Advanced UI  
    
    path('ui-ribbon', app_views.ui_ribbon, name='ui_ribbon'),
    path('ui-clipboard', app_views.ui_clipboard, name='ui_clipboard'),
    path('ui-drag-drop', app_views.ui_drag_drop, name='ui_drag_drop'),
    path('ui-rangeslider', app_views.ui_rangeslider, name='ui_rangeslider'),
    path('ui-rating', app_views.ui_rating, name='ui_rating'),
    path('ui-text-editor', app_views.ui_text_editor, name='ui_text_editor'),
    path('ui-counter', app_views.ui_counter, name='ui_counter'),
    path('ui-scrollbar', app_views.ui_scrollbar, name='ui_scrollbar'),
    path('ui-stickynote', app_views.ui_stickynote, name='ui_stickynote'),
    path('ui-timeline', app_views.ui_timeline, name='ui_timeline'),
    
    #Charts
    
    path('chart-apex', app_views.chart_apex, name='chart_apex'),
    path('chart-c3', app_views.chart_c3, name='chart_c3'),
    path('chart-js', app_views.chart_js, name='chart_js'),
    path('chart-morris', app_views.chart_morris, name='chart_morris'),
    path('chart-flot', app_views.chart_flot, name='chart_flot'),
    path('chart-peity', app_views.chart_peity, name='chart_peity'),
    
    #Icons
    
    path('icon-fontawesome', app_views.icon_fontawesome, name='icon_fontawesome'),
    path('icon-feather', app_views.icon_feather, name='icon_feather'),
    path('icon-ionic', app_views.icon_ionic, name='icon_ionic'),
    path('icon-material', app_views.icon_material, name='icon_material'),
    path('icon-pe7', app_views.icon_pe7, name='icon_pe7'),
    path('icon-simpleline', app_views.icon_simpleline, name='icon_simpleline'),
    path('icon-themify', app_views.icon_themify, name='icon_themify'),
    path('icon-weather', app_views.icon_weather, name='icon_weather'),
    path('icon-typicon', app_views.icon_typicon, name='icon_typicon'),
    path('icon-flag', app_views.icon_flag, name='icon_flag'),
    
    #Forms
    
    path('form-basic-inputs', app_views.form_basic_inputs, name='form_basic_inputs'),
    path('form-checkbox-radios', app_views.form_checkbox_radios, name='form_checkbox_radios'),
    path('form-input-groups', app_views.form_input_groups, name='form_input_groups'),
    path('form-grid-gutters', app_views.form_grid_gutters, name='form_grid_gutters'),
    path('form-select', app_views.form_select, name='form_select'),
    path('form-mask', app_views.form_mask, name='form_mask'),
    path('form-fileupload', app_views.form_fileupload, name='form_fileupload'),
    path('form-elements', app_views.form_elements, name='form_elements'),
    path('form-horizontal', app_views.form_horizontal, name='form_horizontal'),
    path('form-vertical', app_views.form_vertical, name='form_vertical'),
    path('form-floating-labels', app_views.form_floating_labels, name='form_floating_labels'),
    path('form-validation', app_views.form_validation, name='form_validation'),
    path('form-select2', app_views.form_select2, name='form_select2'),
    path('form-wizard', app_views.form_wizard, name='form_wizard'),
    
    #Tables
    
    path('tables-basic', app_views.tables_basic, name='tables_basic'),
    path('data-tables', app_views.data_tables, name='data_tables'),
    
    #Support
    
    path('contact-messages', app_views.contact_messages, name='contact_messages'),
    path('tickets', app_views.tickets, name='tickets'),
    path('ticket-grid', app_views.ticket_grid, name='ticket_grid'),
    path('ticket-details', app_views.ticket_details, name='ticket_details'),

    #Academic

    path('classes-list', app_views.classes_list, name='classes_list'),
    path('schedule-classes', app_views.schedule_classes, name='schedule_classes'),
    path('class-room', app_views.class_room, name='class_room'),
    path('class-routine', app_views.class_routine, name='class_routine'),
    path('class-section', app_views.class_section, name='class_section'),
    path('class-subject', app_views.class_subject, name='class_subject'),
    path('class-syllabus', app_views.class_syllabus, name='class_syllabus'),
    path('class-time-table', app_views.class_time_table, name='class_time_table'),
    path('class-home-work', app_views.class_home_work, name='class_home_work'),
    path('academic-reasons', app_views.academic_reasons, name='academic_reasons'),
    path('exam-list', app_views.exam_list, name='exam_list'),
    path('exam-schedule', app_views.exam_schedule, name='exam_schedule'),
    path('grade', app_views.grade, name='grade'),
    path('exam-attendance', app_views.exam_attendance, name='exam_attendance'),
    path('exam-results', app_views.exam_results, name='exam_results'),

    # HRM

    path('staffs-list', app_views.staffs_list, name='staffs_list'),
    path('add-staff', app_views.add_staff, name='add_staff'),
    path('edit-staff', app_views.edit_staff, name='edit_staff'),
    path('departments', app_views.departments, name='departments'),
    path('designation', app_views.designation, name='designation'),
    path('student-attendance', app_views.student_attendance, name='student_attendance'),
    path('teacher-attendance', app_views.teacher_attendance, name='teacher_attendance'),
    path('staff-attendance', app_views.staff_attendance, name='staff_attendance'),
    path('list-leaves', app_views.list_leaves, name='list_leaves'),
    path('approve-request', app_views.approve_request, name='approve_request'),
    path('holidays', app_views.holidays, name='holidays'),
    path('payroll', app_views.payroll, name='payroll'),
    path('staff-details', app_views.staff_details, name="staff_details"),
    path('staff-payroll', app_views.staff_payroll, name="staff_payroll"),
    path('staff-leaves', app_views.staff_leaves, name="staff_leaves"),
    path('staffs-attendance', app_views.staffs_attendance, name="staffs_attendance"),

    # Finance & Accounts

    path('expenses', app_views.expenses, name='expenses'),
    path('expenses-category', app_views.expenses_category, name='expenses_category'),
    path('accounts-income', app_views.accounts_income, name='accounts_income'),
    path('accounts-invoices', app_views.accounts_invoices, name='accounts_invoices'),
    path('invoice', app_views.invoice, name='invoice'),
    path('accounts-transactions', app_views.accounts_transactions, name='accounts_transactions'),
    path('add-invoice', app_views.add_invoice, name='add_invoice'),
    path('edit-invoice', app_views.edit_invoice, name='edit_invoice'),
    
    # Announcements

    path('notice-board', app_views.notice_board, name='notice_board'),
    path('events', app_views.events, name='events'),

    # Reports

    path('attendance-report', app_views.attendance_report, name='attendance_report'),
    path('student-attendance-type', app_views.student_attendance_type, name='student_attendance_type'),
    path('daily-attendance', app_views.daily_attendance, name='daily_attendance'),
    path('student-day-wise', app_views.student_day_wise, name='student_day_wise'),
    path('teacher-day-wise', app_views.teacher_day_wise, name='teacher_day_wise'),
    path('teacher-report', app_views.teacher_report, name='teacher_report'),
    path('staff-day-wise', app_views.staff_day_wise, name='staff_day_wise'),
    path('staff-report', app_views.staff_report, name='staff_report'),
    path('class-report', app_views.class_report, name='class_report'),
    path('student-report', app_views.student_report, name='student_report'),
    path('grade-report', app_views.grade_report, name='grade_report'),
    path('leave-report', app_views.leave_report, name='leave_report'),
    path('fees-report', app_views.fees_report, name='fees_report'),

    # User Management

    path('users', app_views.users, name='users'),
    path('roles-permission', app_views.roles_permission, name='roles_permission'),
    path('permission', app_views.permission, name='permission'),
    path('delete-account', app_views.delete_account, name='delete_account'),

    # Membership

    path('membership-plans', app_views.membership_plans, name="membership_plans"),
    path('membership-addons', app_views.membership_addons, name="membership_addons"),
    path('membership-transactions', app_views.membership_transactions, name="membership_transactions"),

    # Layout

    path('layout-default', app_views.layout_default, name="layout_default"),
    path('layout-mini', app_views.layout_mini, name="layout_mini"),
    path('layout-rtl', app_views.layout_rtl, name="layout_rtl"),
    path('layout-box', app_views.layout_box, name="layout_box"),
    path('layout-dark', app_views.layout_dark, name="layout_dark"),
    
    path('activites', app_views.activites, name="activites"),

    # pages
    
    path('under-maintenance', app_views.under_maintenance, name="under_maintenance"),
    path('coming-soon', app_views.coming_soon, name="coming_soon"),
    path('profile', app_views.profile, name="profile"),
    path('lock-screen', app_views.lock_screen, name="lock_screen"),
    path('blank-page', app_views.blank_page, name="blank_page"),
    path('404-error', app_views.error_404, name="error_404"),
    path('500-error', app_views.error_500, name="error_500"),
]
