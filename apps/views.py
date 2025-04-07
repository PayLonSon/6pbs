from django.shortcuts import render

# Create your views here.

  # Authentication

def login(request):
    return render(request, 'auth/login.html')

def login_two(request):
    return render(request, 'auth/login-2.html')

def login_three(request):
    return render(request, 'auth/login-3.html')

def register(request):
    return render(request, 'auth/register.html')

def register_two(request):
    return render(request, 'auth/register-2.html')

def register_three(request):
    return render(request, 'auth/register-3.html')

def forgot_password(request):
    return render(request, 'auth/forgot-password.html')

def forgot_password_two(request):
    return render(request, 'auth/forgot-password-2.html')

def forgot_password_three(request):
    return render(request, 'auth/forgot-password-3.html')

def reset_password(request):
    return render(request, 'auth/reset-password.html')

def reset_password_two(request):
    return render(request, 'auth/reset-password-2.html')

def reset_password_three(request):
    return render(request, 'auth/reset-password-3.html')

def reset_password_success(request):
    return render(request, 'auth/reset-password-success.html')

def reset_password_success_two(request):
    return render(request, 'auth/reset-password-success-2.html')

def reset_password_success_three(request):
    return render(request, 'auth/reset-password-success-3.html')

def email_verification(request):
    return render(request, 'auth/email-verification.html')

def email_verification_two(request):
    return render(request, 'auth/email-verification-2.html')

def email_verification_three(request):
    return render(request, 'auth/email-verification-3.html')

def two_step_verification(request):
    return render(request, 'auth/two-step-verification.html')

def two_step_verification_two(request):
    return render(request, 'auth/two-step-verification-2.html')

def two_step_verification_three(request):
    return render(request, 'auth/two-step-verification-3.html')

# Application
    
def chat(request):
    return render(request, 'pages/application/chat.html')
 
def call(request):
    return render(request, 'pages/application/call.html')
 
def calendar(request):
    return render(request, 'pages/application/calendar.html')
 
def email(request):
    return render(request, 'pages/application/email.html')
 
def todo(request):
    return render(request, 'pages/application/todo.html')
 
def notes(request):
    return render(request, 'pages/application/notes.html')
 
def file_manager(request):
    return render(request, 'pages/application/file-manager.html')
 
def video_call(request):
    return render(request, 'pages/application/video-call.html')
 
#Content

def pages(request):
    pages = [
  {
    "Page": "Students",
    "PageSlug": "students",
    "Id": "user1",
    "For": "user1",
  },
  {
    "Page": "Teachers",
    "PageSlug": "teachers",
    "Id": "user2",
    "For": "user2",
  },
  {
    "Page": "Parents",
    "PageSlug": "parents",
    "Id": "user3",
    "For": "user3",
  },
  {
    "Page": "Guardians",
    "PageSlug": "guardians",
    "Id": "user4",
    "For": "user4",
  },
  {
    "Page": "Classes",
    "PageSlug": "classes",
    "Id": "user5",
    "For": "user5",
  },
  {
    "Page": "Hostel",
    "PageSlug": "hostel",
    "Id": "user6",
    "For": "user6",
  },
]
    return render(request, 'pages/content/pages.html', {'pages' : pages})
 
def blog(request):
    return render(request, 'pages/content/blog/blog.html')

def blog_categories(request):
    blog_categories = [
        {
            "Category": "Education",
            "Addedon": "25 May 2024",
            "Status": "Active",
        },
        {
            "Category": "Advice",
            "Addedon": "24 May 2024",
            "Status": "Active",
        },
        {
            "Category": "Academic",
            "Addedon": "15 Mar 2024",
            "Status": "Active",
        },
        {
            "Category": "Clear Goals",
            "Addedon": "21 Feb 2024",
            "Status": "Active",
        },
        {
            "Category": "Healthy Education",
            "Addedon": "15 Feb 2024",
            "Status": "Inactive",
        },
        {
            "Category": "Transport",
            "Addedon": "12 Feb 2024",
            "Status": "Active",
        },
        {
            "Category": "Hostel",
            "Addedon": "14 Jan 2024",
            "Status": "Active",
        },
        {
            "Category": "Management",
            "Addedon": "12 Jan 2024",
            "Status": "Active",
        },
        {
            "Category": "Guidance",
            "Addedon": "16 Dec 2023",
            "Status": "Inactive",
        },
        {
            "Category": "Sports",
            "Addedon": "12 Dec 2023",
            "Status": "Active",
        },
        ]
    return render(request, 'pages/content/blog/blog-categories.html', {'blog_categories' : blog_categories})

def blog_comments(request):
    return render(request, 'pages/content/blog/blog-comments.html')

def blog_tags(request):
    blog_tags = [
        {
            "Tags": "Guide",
            "Addedon": "25 May 2024",
            "Status": "Active",
        },
        {
            "Tags": "Development",
            "Addedon": "24 May 2024",
            "Status": "Active",
        },
        {
            "Tags": "Education",
            "Addedon": "15 Mar 2024",
            "Status": "Active",
        },
        {
            "Tags": "Chances",
            "Addedon": "21 Feb 2024",
            "Status": "Active",
        },
        {
            "Tags": "Management",
            "Addedon": "15 Feb 2024",
            "Status": "Inactive",
        },
        {
            "Tags": "Sports",
            "Addedon": "12 Feb 2024",
            "Status": "Active",
        },
        {
            "Tags": "Guidance",
            "Addedon": "14 Jan 2024",
            "Status": "Active",
        },
        {
            "Tags": "Location",
            "Addedon": "12 Jan 2024",
            "Status": "Active",
        },
        {
            "Tags": "Hostel",
            "Addedon": "16 Dec 2023",
            "Status": "Inactive",
        },
        {
            "Tags": "Academic",
            "Addedon": "12 Dec 2023",
            "Status": "Active",
        },
        ]
    return render(request, 'pages/content/blog/blog-tags.html', {'blog_tags' : blog_tags})

def countries(request):
    countries = [
        {
            "ID": "CO378258",
            "CountryName": "United States",
            "CountryCode": "US",
            "Status": "Active",
        },
        {
            "ID": "CO378257",
            "CountryName": "Canada",
            "CountryCode": "CA",
            "Status": "Active",
        },
        {
            "ID": "CO378256",
            "CountryName": "United Kingdom",
            "CountryCode": "UK",
            "Status": "Active",
        },
        {
            "ID": "CO378255",
            "CountryName": "Germany",
            "CountryCode": "DE",
            "Status": "Active",
        },
        {
            "ID": "CO378254",
            "CountryName": "France",
            "CountryCode": "FR",
            "Status": "Active",
        },
        {
            "ID": "CO378253",
            "CountryName": "Argentina",
            "CountryCode": "AR",
            "Status": "Active",
        },
        {
            "ID": "CO378252",
            "CountryName": "India",
            "CountryCode": "IN",
            "Status": "Active",
        },
        {
            "ID": "CO378251",
            "CountryName": "Argentina",
            "CountryCode": "AR",
            "Status": "Active",
        },
        {
            "ID": "CO378250",
            "CountryName": "New Zealand",
            "CountryCode": "NZ",
            "Status": "Active",
        },
        {
            "ID": "CO378249",
            "CountryName": "Australia",
            "CountryCode": "AU",
            "Status": "Active",
        },
        ]
    return render(request, 'pages/content/location/countries.html', {'countries' : countries})

def states(request):
    states = [
        {
            "ID": "ST364285",
            "StateName": "California",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "ST364284",
            "StateName": "New York",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "ST364283",
            "StateName": "Texas",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "ST364282",
            "StateName": "Bavaria",
            "CountryName": "Germany",
            "Status": "Active",
        },
        {
            "ID": "ST364281",
            "StateName": "Quebec",
            "CountryName": "Canada",
            "Status": "Active",
        },
        {
            "ID": "ST364280",
            "StateName": "Ontario",
            "CountryName": "Canada",
            "Status": "Active",
        },
        {
            "ID": "ST364279",
            "StateName": "Florida",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "ST364278",
            "StateName": "Berlin",
            "CountryName": "Germany",
            "Status": "Active",
        },
        {
            "ID": "ST364277",
            "StateName": "Victoria",
            "CountryName": "Australia",
            "Status": "Active",
        },
        {
            "ID": "ST364276",
            "StateName": "Gauteng",
            "CountryName": "Egypt",
            "Status": "Active",
        },
        ]
    return render(request, 'pages/content/location/states.html', {'states' : states})

def cities(request):
    cities = [
        {
            "ID": "CI357268",
            "CityName": "Los Angeles",
            "StateName": "California",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "CI357267",
            "CityName": "New York City",
            "StateName": "New York",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "CI357266",
            "CityName": "Houston",
            "StateName": "Texas",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "CI357265",
            "CityName": "Munich",
            "StateName": "Bavaria",
            "CountryName": "Germany",
            "Status": "Active",
        },
        {
            "ID": "CI357264",
            "CityName": "Montreal",
            "StateName": "Quebec",
            "CountryName": "Canada",
            "Status": "Active",
        },
        {
            "ID": "CI357263",
            "CityName": "Toronto",
            "StateName": "Ontario",
            "CountryName": "Canada",
            "Status": "Active",
        },
        {
            "ID": "CI357262",
            "CityName": "Miami",
            "StateName": "Florida",
            "CountryName": "United States",
            "Status": "Active",
        },
        {
            "ID": "CI357261",
            "CityName": "Calgary",
            "StateName": "Berlin",
            "CountryName": "Germany",
            "Status": "Active",
        },
        {
            "ID": "CI357260",
            "CityName": "Melbourne",
            "StateName": "Victoria",
            "CountryName": "Australia",
            "Status": "Active",
        },
        {
            "ID": "CI357259",
            "CityName": "Johannesburg",
            "StateName": "Gauteng",
            "CountryName": "Egypt",
            "Status": "Active",
        },
        ]
    return render(request, 'pages/content/location/cities.html', {'cities' : cities})

def testimonials(request):
    testimonials = [
        {
            "ID": "T346285",
            "Author": "Thomas",
            "Role": "Parent",
            "Content": "I'm impressed with how easy it is to track my child's progress using this system.",
            "DateAdded": "25 Apr 2024",
            "Image": "assets/img/parents/parent-01.jpg",
        },
        {
            "ID": "T346284",
            "Author": "Teresa",
            "Role": "Teacher",
            "Content": "The gradebook feature has streamlined my grading process”",
            "DateAdded": "28 Apr 2024",
            "Image": "assets/img/teachers/teacher-01.jpg",
        },
        {
            "ID": "T346283",
            "Author": "Veronica",
            "Role": "Student",
            "Content": "I find the timetable feature very helpful in keeping track of my classes and assignments.",
            "DateAdded": "02 May 2024",
            "Image": "assets/img/students/student-11.jpg",
        },
        {
            "ID": "T346282",
            "Author": "Kevin",
            "Role": "Admin",
            "Content": "Our school has seen a significant improvement in efficiency since implementing this system.",
            "DateAdded": "14 May 2024",
            "Image": "assets/img/profiles/avatar-27.jpg",
        },
        {
            "ID": "T346281",
            "Author": "Claudia",
            "Role": "Parent",
            "Content": "The communication tools have made it much easier to stay informed about school events”",
            "DateAdded": "20 May 2024",
            "Image": "assets/img/parents/parent-04.jpg",
        },
        {
            "ID": "T346280",
            "Author": "Hellana",
            "Role": "Teacher",
            "Content": "I appreciate the support provided by the technical team in customizing the system”",
            "DateAdded": "05 Jun 2024",
            "Image": "assets/img/teachers/teacher-03.jpg",
        },
        {
            "ID": "T346279",
            "Author": "Robert",
            "Role": "Parent",
            "Content": "The online payment system has made fee payments hassle-free.Great addition to the system!",
            "DateAdded": "16 Jun 2024",
            "Image": "assets/img/parents/parent-07.jpg",
        },
        {
            "ID": "T346278",
            "Author": "Kevin",
            "Role": "Admin",
            "Content": "The system's user interface is intuitive and easy to navigate,even for non-technical users.",
            "DateAdded": "21 Jun 2024",
            "Image": "assets/img/profiles/avatar-27.jpg",
        },
        {
            "ID": "T346277",
            "Author": "Michael",
            "Role": "Parent",
            "Content": "The parent-teacher communication portal has facilitated open dialogue and collaboration”",
            "DateAdded": "10 Jul 2024",
            "Image": "assets/img/parents/parent-09.jpg",
        },
        {
            "ID": "T346276",
            "Author": "Aaron",
            "Role": "Teacher",
            "Content": "The system's lesson planning tools have helped me organize and deliver more effective lessons.",
            "DateAdded": "12 Jul 2024",
            "Image": "assets/img/teachers/teacher-06.jpg",
        },
        ]
    return render(request, 'pages/content/testimonials.html', {'testimonials' : testimonials})

def faq(request):
    faq = [
        {
            "ID": "T374832",
            "Questions": "How do I reset my password?",
            "Answers": "You can reset your password from the login page.",
            "Category": "Account",
        },
        {
            "ID": "T374831",
            "Questions": "How do I update my contact information?",
            "Answers": 'You can update your contact information in the "My Account"',
            "Category": "Account",
        },
        {
            "ID": "T374830",
            "Questions": "How can I contact the IT support team?",
            "Answers": "Contact support via email at support@example.com",
            "Category": "Support",
        },
        {
            "ID": "T374829",
            "Questions": "Where can I find information about school events?",
            "Answers": "Information is available on the website's Events page",
            "Category": "Events",
        },
        {
            "ID": "T374828",
            "Questions": "How do I access online learning resources?",
            "Answers": "Access resources through the school's LMS",
            "Category": "Academic",
        },
        {
            "ID": "T374827",
            "Questions": "Where can I find information about school fees?",
            "Answers": "Information is available on the Fees & Payments page",
            "Category": "Finance",
        },
        {
            "ID": "T374826",
            "Questions": "How do I register for extracurricular activities?",
            "Answers": "Register through the school portal's Extracurriculars section.",
            "Category": "Academic",
        },
        {
            "ID": "T374825",
            "Questions": "Can I volunteer at the school?",
            "Answers": "Yes, volunteering opportunities are available at the school.",
            "Category": "General",
        },
        {
            "ID": "T374824",
            "Questions": "What are the school's hours of operation?",
            "Answers": "School hours vary by department and are typically posted",
            "Category": "Academic",
        },
        {
            "ID": "T346285",
            "Questions": "How can I request a tour of the school campus?",
            "Answers": "Contact the admissions office to schedule a tour with a staff",
            "Category": "General",
        },
        ]
    return render(request, 'pages/content/faq.html', {'faq' : faq})

#Settings
    
def profile_settings(request):
    return render(request, 'pages/settings/general-settings/profile-settings.html')
 
def security_settings(request):
    return render(request, 'pages/settings/general-settings/security-settings.html')
 
def notifications_settings(request):
    return render(request, 'pages/settings/general-settings/notifications-settings.html')
 
def connected_apps(request):
    return render(request, 'pages/settings/general-settings/connected-apps.html')
 
def company_settings(request):
    return render(request, 'pages/settings/website-settings/company-settings.html')
 
def localization(request):
    return render(request, 'pages/settings/website-settings/localization.html')
 
def prefixes(request):
    return render(request, 'pages/settings/website-settings/prefixes.html')
 
def preferences(request):
    return render(request, 'pages/settings/website-settings/preferences.html')
 
def social_authentication(request):
    return render(request, 'pages/settings/website-settings/social-authentication.html')
 
def language(request):
    return render(request, 'pages/settings/website-settings/language.html')
 
def invoice_settings(request):
    return render(request, 'pages/settings/app-settings/invoice-settings.html')
 
def custom_fields(request):
    return render(request, 'pages/settings/app-settings/custom-fields.html')
 
def email_settings(request):
    return render(request, 'pages/settings/system-settings/email-settings.html')
 
def email_templates(request):
    return render(request, 'pages/settings/system-settings/email-templates.html')
 
def sms_settings(request):
    return render(request, 'pages/settings/system-settings/sms-settings.html')
 
def otp_settings(request):
    return render(request, 'pages/settings/system-settings/otp-settings.html')
 
def gdpr_cookies(request):
    return render(request, 'pages/settings/system-settings/gdpr-cookies.html')
 
def payment_gateways(request):
    return render(request, 'pages/settings/financial-settings/payment-gateways.html')
 
def tax_rates(request):
    return render(request, 'pages/settings/financial-settings/tax-rates.html')
 
def school_settings(request):
    return render(request, 'pages/settings/academic-settings/school-settings.html')
 
def religion(request):
    return render(request, 'pages/settings/academic-settings/religion.html')
 
def storage(request):
    return render(request, 'pages/settings/other-settings/storage.html')
 
def ban_ip_address(request):
    return render(request, 'pages/settings/other-settings/ban-ip-address.html')
 
 
# Management
    
def fees_group(request):
    fees_group = [
        {
            "ID": "FG80482",
            "FeesGroup": "Tuition Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Monthly Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80480",
            "FeesGroup": "Class 1 General",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80479",
            "FeesGroup": "Class 1 Lump Sum",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80478",
            "FeesGroup": "Class 1- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Inactive",
        },
        {
            "ID": "FG80477",
            "FeesGroup": "Class 1-II Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80476",
            "FeesGroup": "Class 1-III Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80475",
            "FeesGroup": "Discount",
            "Description": "The money that you pay to be taught",
            "Status": "Inactive",
        },
        {
            "ID": "FG80474",
            "FeesGroup": "Class 3- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80473",
            "FeesGroup": "Class 4- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80482",
            "FeesGroup": "Tuition Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Monthly Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        }
    ]
    return render(request, 'pages/management/fees/fees-group.html', {'fees_group': fees_group})

    # Peoples

def fees_type(request):
    fees_type = [
        {
            "ID": "FG80482",
            "FeesType": "Admission Fees",
            "FeesCode": "Admission-Fees",
            "FeesGroup": "Tuition Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80481",
            "FeesType": "Apr-Mar",
            "FeesCode": "Apr-Mar",
            "FeesGroup": "Monthly Fees",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80480",
            "FeesType": "Bus Fees",
            "FeesCode": "Bus-Fees",
            "FeesGroup": "Class 1 General",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80479",
            "FeesType": "1st Installment Fees",
            "FeesCode": "1st-Installment-Fees",
            "FeesGroup": "Class 1 Lump Sum",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80478",
            "FeesType": "2nd Installment Fees",
            "FeesCode": "2nd-Installment-Fees",
            "FeesGroup": "Class 1- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Inactive",
        },
        {
            "ID": "FG80477",
            "FeesType": "3rd Installment Fees",
            "FeesCode": "3rd-Installment-Fees",
            "FeesGroup": "Class 1-II Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80476",
            "FeesType": "4th Installment Fees",
            "FeesCode": "3rd-Installment-Fees",
            "FeesGroup": "Class 1-III Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80475",
            "FeesType": "Topper Discount",
            "FeesCode": "3rd-Installment-Fees",
            "FeesGroup": "Discount",
            "Description": "The money that you pay to be taught",
            "Status": "Inactive",
        },
        {
            "ID": "FG80474",
            "FeesType": "3rd Installment Fees",
            "FeesCode": "3rd-Installment-Fees",
            "FeesGroup": "Class 3- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        },
        {
            "ID": "FG80473",
            "FeesType": "4th Installment Fees",
            "FeesCode": "4th-Installment-Fees",
            "FeesGroup": "Class 4- I Installment",
            "Description": "The money that you pay to be taught",
            "Status": "Active",
        }
        ]
    return render(request, 'pages/management/fees/fees-type.html', {'fees_type': fees_type})

def fees_master(request):
    fees_master = [
        {
            "ID": "FG80482",
            "FeesGroup": "Admission-Fees",
            "FeesType": "Tuition Fees",
            "DueDate": "30 Jan 2025",
            "Amount": "1250",
            "FineType": "None",
            "FineClass": "badge badge-soft-warning",
            "FineAmount": "200",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 1 General",
            "FeesType": "Monthly Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Percentage",
            "FineClass": "badge badge-soft-info",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Monthly Fees",
            "FeesType": "Admission Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Percentage",
            "FineClass": "badge badge-soft-info",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 1 Lump Sum",
            "FeesType": "Bus Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Percentage",
            "FineClass": "badge badge-soft-info",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 1- I Installment",
            "FeesType": "Monthly Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Fixed",
            "FineClass": "badge badge-soft-danger",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 1-II Installment",
            "FeesType": "Monthly Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Percentage",
            "FineClass": "badge badge-soft-info",
            "FineAmount": "300",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Discount",
            "FeesType": "Topper Discount",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "None",
            "FineClass": "badge badge-soft-warning",
            "FineAmount": "300",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 3- I Installment",
            "FeesType": "3rd-Installment-Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "None",
            "FineClass": "badge badge-soft-warning",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "FG80481",
            "FeesGroup": "Class 2- I Installment",
            "FeesType": "3rd-Installment-Fees",
            "DueDate": "12 May 2025",
            "Amount": "250",
            "FineType": "Fixed",
            "FineClass": "badge badge-soft-danger",
            "FineAmount": "300",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
                "ID": "FG80481",
                "FeesGroup": "Class 4- I Installment",
                "FeesType": "3rd Installment Fees",
                "DueDate": "12 May 2025",
                "Amount": "250",
                "FineType": "Fixed",
                "FineClass": "badge badge-soft-danger",
                "FineAmount": "300",
                "Status": "Active",
                "StatusClass": "badge badge-soft-success",
        },
    ]
    
    return render(request, 'pages/management/fees/fees-master.html', {'fees_master': fees_master})

def fees_assign(request):
    fees_assign = [
        {
            "SNo": "1",
            "FeesGroup": "Admission-Fees",
            "FeesType": "Tuition Fees",
            "Class": "I",
            "Section": "B",
            "Amount": "1250",
            "Gender": "Male",
            "Category": "BC",
        },
        {
            "SNo": "2",
            "FeesGroup": "Class 1 General",
            "FeesType": "Monthly Fees",
            "Class": "III",
            "Section": "C",
            "Amount": "250",
            "Gender": "Both",
            "Category": "MBC",
        },
        {
            "SNo": "3",
            "FeesGroup": "Monthly Fees",
            "FeesType": "Admission Fees",
            "Class": "IX",
            "Section": "F",
            "Amount": "656",
            "Gender": "Female",
            "Category": "FC",
        },
        {
            "SNo": "4",
            "FeesGroup": "Class 1 Lump Sum",
            "FeesType": "Bus Fees",
            "Class": "X",
            "Section": "R",
            "Amount": "6225",
            "Gender": "Male",
            "Category": "BC",
        },
        {
            "SNo": "5",
            "FeesGroup": "Class 1- I Installment",
            "FeesType": "Monthly Fees",
            "Class": "III",
            "Section": "E",
            "Amount": "454",
            "Gender": "Both",
            "Category": "MBC",
        },
        {
            "SNo": "6",
            "FeesGroup": "Class 1-II Installment",
            "FeesType": "Monthly Fees",
            "Class": "IV",
            "Section": "A",
            "Amount": "214",
            "Gender": "Male",
            "Category": "All",
        },
        {
            "SNo": "7",
            "FeesGroup": "Discount",
            "FeesType": "Topper Discount",
            "Class": "V",
            "Section": "B",
            "Amount": "145",
            "Gender": "Both",
            "Category": "FC",
        },
        {
            "SNo": "8",
            "FeesGroup": "Class 3- I Installment",
            "FeesType": "3rd-Installment-Fees",
            "Class": "X",
            "Section": "B",
            "Amount": "147",
            "Gender": "Male",
            "Category": "FC",
        },
        {
            "SNo": "9",
            "FeesGroup": "Class 2- I Installment",
            "FeesType": "3rd-Installment-Fees",
            "Class": "VI",
            "Section": "A",
            "Amount": "457",
            "Gender": "Female",
            "Category": "FC",
        },
        {
            "SNo": "10",
            "FeesGroup": "Class 4- I Installment",
            "FeesType": "3rd Installment Fees",
            "Class": "V",
            "Section": "A",
            "Amount": "654",
            "Gender": "Female",
            "Category": "All",
        },
]
    return render(request, 'pages/management/fees/fees-assign.html', {'fees_assign': fees_assign})

def collect_fees(request):
    collect_fees = [
        {
            "AdmNo": "AD124556",
            "RollNo": "55365",
            "Student": "Janet",
            "StudentClass": "III, A",
            "Class": "III",
            "Section": "A",
            "StudentImage": "assets/img/students/student-01.jpg",
            "Parent": "Thomas",
            "ParentClass": "Added on 25 Mar 2024",
            "Email": "thomas@example.com",
            "Amount": "2000",
            "LastDate": "15 May 2024",
            "Status": "Paid",
            "StatusClass": "badge badge-soft-success",
            "View": "View Details",
        },
        {
            "AdmNo": "AD124555",
            "RollNo": "12454",
            "Student": "Joann",
            "StudentClass": "IV, B",
            "Class": "IV",
            "Section": "B",
            "StudentImage": "assets/img/students/student-02.jpg",
            "Parent": "Marquita",
            "ParentClass": "Added on 18 Mar 2024",
            "Email": "marquita@example.com",
            "Amount": "156",
            "LastDate": "15 May 2024",
            "Status": "Paid",
            "StatusClass": "badge badge-soft-success",
            "View": "View Details",
        },
        {
            "AdmNo": "AD124554",
            "RollNo": "65454",
            "Student": "Kathleen",
            "StudentClass": "III, A",
            "Class": "III",
            "Section": "A",
            "StudentImage": "assets/img/students/student-03.jpg",
            "Parent": "Johnson",
            "ParentClass": "Added on 14 Mar 2024",
            "Email": "johnson@example.com",
            "Amount": "645",
            "LastDate": "15 May 2024",
            "Status": "Paid",
            "StatusClass": "badge badge-soft-success",
            "View": "View Details",
        },
        {
            "AdmNo": "AD124553",
            "RollNo": "78787",
            "Student": "Gifford",
            "StudentClass": "I, B",
            "Class": "I",
            "Section": "B",
            "StudentImage": "assets/img/students/student-04.jpg",
            "Parent": "Claudia",
            "ParentClass": "Added on 27 Feb 2024",
            "Email": "claudia@example.com",
            "Amount": "456",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "AD124552",
            "RollNo": "31564",
            "Student": "Lisa",
            "StudentClass": "II, B",
            "Class": "II",
            "Section": "B",
            "StudentImage": "assets/img/students/student-05.jpg",
            "Parent": "Arthur",
            "ParentClass": "Added on 11 Feb 2024",
            "Email": "arthur@example.com",
            "Amount": "645",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "AD124551",
            "RollNo": "78456",
            "Student": "Ralph",
            "StudentClass": "III, B",
            "Class": "III",
            "Section": "B",
            "StudentImage": "assets/img/students/student-06.jpg",
            "Parent": "Colleen",
            "ParentClass": "Added on 24 Jan 2024",
            "Email": "colleen@example.com",
            "Amount": "156",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "AD124550",
            "RollNo": "67897",
            "Student": "Julie",
            "StudentClass": "V, A",
            "Class": "III",
            "Section": "B",
            "StudentImage": "assets/img/students/student-07.jpg",
            "Parent": "Robert",
            "ParentClass": "Added on 19 Jan 2024",
            "Email": "colleen@example.com",
            "Amount": "156",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "P124549",
            "RollNo": "47895",
            "Student": "Ryan",
            "StudentClass": "VI, A",
            "Class": "VI",
            "Section": "A",
            "StudentImage": "assets/img/students/student-08.jpg",
            "Parent": "Jessie",
            "ParentClass": "Added on 08 Jan 2024",
            "Email": "jessie@example.com",
            "Amount": "645",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "AD124548",
            "RollNo": "65547",
            "Student": "Susan",
            "StudentClass": "VIII, B",
            "Class": "VIII",
            "Section": "B",
            "StudentImage": "assets/img/students/student-09.jpg",
            "Parent": "Michael",
            "ParentClass": "Added on 22 Dec 2023",
            "Email": "michael@example.com",
            "Amount": "456",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "View Details",
        },
        {
            "AdmNo": "AD124548",
            "RollNo": "65547",
            "Student": "Richard",
            "StudentClass": "Richard",
            "Class": "VII",
            "Section": "B",
            "StudentImage": "assets/img/students/student-10.jpg",
            "Parent": "Mary",
            "ParentClass": "Added on 15 Dec 2024",
            "Email": "mary@example.com",
            "Amount": "456",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
        {
            "AdmNo": "AD124548",
            "RollNo": "65547",
            "Student": "Susan",
            "StudentClass": "VIII, B",
            "Class": "VIII",
            "Section": "B",
            "StudentImage": "assets/img/students/student-09.jpg",
            "Parent": "Michael",
            "ParentClass": "Added on 22 Dec 2023",
            "Email": "michael@example.com",
            "Amount": "456",
            "LastDate": "15 May 2024",
            "Status": "Unpaid",
            "StatusClass": "badge badge-soft-danger",
            "View": "Collect Fees",
        },
]
    return render(request, 'pages/management/fees/collect-fees.html', {'collect_fees': collect_fees})

def library_members(request):
    library_members = [
        {
            "ID": "LM823748",
            "Member": "James",
            "MemberImage": "assets/img/members/members-01.jpg",
            "CardNo": "501",
            "Email": '"james@example.com',
            "DateofJoin": "22 Apr 2024",
            "Mobile": "+1 78429 82414",
        },
        {
            "ID": "LM823747",
            "Member": "Garcia",
            "MemberImage": "assets/img/members/members-02.jpg",
            "CardNo": "502",
            "Email": "garcia@example.com",
            "DateofJoin": "30 Apr 2024",
            "Mobile": "+1 37489 46485",
        },
        {
            "ID": "LM823746",
            "Member": "Frank",
            "MemberImage": "assets/img/members/members-03.jpg",
            "CardNo": "503",
            "Email": "frank@example.com",
            "DateofJoin": "05 May 2024",
            "Mobile": "+1 87651 64816",
        },
        {
            "ID": "LM823745",
            "Member": "Jennie",
            "MemberImage": "assets/img/members/members-04.jpg",
            "CardNo": "504",
            "Email": "jennie@example.com",
            "DateofJoin": "16 May 2024",
            "Mobile": "+1 49879 86498",
        },
        {
            "ID": "LM823744",
            "Member": "Paul",
            "MemberImage": "assets/img/members/members-05.jpg",
            "CardNo": "505",
            "Email": "paul@example.com",
            "DateofJoin": "28 May 2024",
            "Mobile": "+1 69787 87984",
        },
        {
            "ID": "LM823743",
            "Member": "Elaine",
            "MemberImage": "assets/img/members/members-06.jpg",
            "CardNo": "506",
            "Email": "elaine@example.com",
            "DateofJoin": "06 Jun 2024",
            "Mobile": "+1 98764 84984",
        },
        {
            "ID": "LM823742",
            "Member": "Jackson",
            "MemberImage": "assets/img/members/members-07.jpg",
            "CardNo": "507",
            "Email": "jackson@example.com",
            "DateofJoin": "10 Jun 2024",
            "Mobile": "+1 46876 55498",
        },
        {
            "ID": "LM823741",
            "Member": "Kerry",
            "MemberImage": "assets/img/members/members-08.jpg",
            "CardNo": "508",
            "Email": "kerry@example.com",
            "DateofJoin": "18 Jun 2024",
            "Mobile": "+1 79468 87467",
        },
        {
            "ID": "LM823740",
            "Member": "Roger",
            "MemberImage": "assets/img/members/members-09.jpg",
            "CardNo": "509",
            "Email": "roger@example.com",
            "DateofJoin": "20 Jul 2024",
            "Mobile": "+1 65598 64658",
        },
        {
            "ID": "LM823739",
            "Member": "Denise",
            "MemberImage": "assets/img/members/members-10.jpg",
            "CardNo": "510",
            "Email": "denise@example.com",
            "DateofJoin": "26 Jul 2024",
            "Mobile": "+1 57866 68746",
        },
]
    return render(request, 'pages/management/library/library-members.html', {'library_members' : library_members})

def library_books(request):
    library_books = [
        {
            "ID": "LB864723",
            "BookName": "Echoes of Eternity",
            "BookNo": "501",
            "Publisher": "Aurora Press",
            "Author": "Isabella Rivers",
            "Subject": "History",
            "RackNo": "6550",
            "Qty": "150",
            "Available": "120",
            "Price": "$300",
            "PostDate": "25 Apr 2024",
        },
        {
            "ID": "LB864722",
            "BookName": "The Stars of Eldorado",
            "BookNo": "502",
            "Publisher": "Nebula Press",
            "Author": "Amanda Grayson",
            "Subject": "Science",
            "RackNo": "6551",
            "Qty": "200",
            "Available": "180",
            "Price": "$280",
            "PostDate": "28 Apr 2024",
        },
        {
            "ID": "LB864722",
            "BookName": "The Glass Painter",
            "BookNo": "503",
            "Publisher": "Artisan Reads",
            "Author": "Isabel Marquez",
            "Subject": "Literary",
            "RackNo": "6552",
            "Qty": "180",
            "Available": "160",
            "Price": "$320",
            "PostDate": "04 May 2024",
        },
        {
            "ID": "LB864720",
            "BookName": "Beyond the Edge",
            "BookNo": "504",
            "Publisher": "Explorer's Press",
            "Author": "Leo Finnegan",
            "Subject": "Adventure",
            "RackNo": "6553",
            "Qty": "120",
            "Available": "100",
            "Price": "$350",
            "PostDate": "18 May 2024",
        },
        {
            "ID": "LB864719",
            "BookName": "Shadow Symphony",
            "BookNo": "505",
            "Publisher": "Harmony House",
            "Author": "Claire Vincent",
            "Subject": "Gothic",
            "RackNo": "6554",
            "Qty": "220",
            "Available": "160",
            "Price": "$280",
            "PostDate": "20 May 2024",
        },
        {
            "ID": "LB864718",
            "BookName": "The Last Library",
            "BookNo": "506",
            "Publisher": "Archive Publishing",
            "Author": "Marcus Brewster",
            "Subject": "Dystopian",
            "RackNo": "6555",
            "Qty": "170",
            "Available": "150",
            "Price": "$250",
            "PostDate": "16 Jun 2024",
        },
        {
            "ID": "LB864717",
            "BookName": "The Saffron Tide",
            "BookNo": "507",
            "Publisher": "Indus Books",
            "Author": "Rajiv Anand",
            "Subject": "History",
            "RackNo": "6556",
            "Qty": "140",
            "Available": "100",
            "Price": "$200",
            "PostDate": "20 Jun 2024",
        },
        {
            "ID": "LB864716",
            "BookName": "Windswept",
            "BookNo": "508",
            "Publisher": "Coastal Press",
            "Author": "Lydia Ramsey",
            "Subject": "Romance",
            "RackNo": "6557",
            "Qty": "300",
            "Available": "270",
            "Price": "$300",
            "PostDate": "24 Jun 2024",
        },
        {
            "ID": "LB864715",
            "BookName": "Frostbound Throne",
            "BookNo": "509",
            "Publisher": "Frozen Realms",
            "Author": "Viktor Korneev",
            "Subject": "Fantasy",
            "RackNo": "6558",
            "Qty": "320",
            "Available": "200",
            "Price": "$350",
            "PostDate": "$10 Jul 2024",
        },
        {
            "ID": "LB864714",
            "BookName": "The Last Alchemist",
            "BookNo": "510",
            "Publisher": "Alchemy Arts",
            "Author": "Philip Dubois",
            "Subject": "Mystery",
            "RackNo": "6559",
            "Qty": "190",
            "Available": "170",
            "Price": "$400",
            "PostDate": "12 Jul 2024",
        },
]
    return render(request, 'pages/management/library/library-books.html', {'library_books' : library_books})

def library_issue_book(request):
    library_issue_book = [
        {
            "ID": "IB853629",
            "DateofIssue": "20 Apr 2024",
            "DueDate": "19 May 2024",
            "IssueTo": "Janet",
            "Class":"III, A",
            "BooksIssued": "1",
            "BookReturned": "0",
            "Image": "assets/img/students/student-01.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853628",
            "DateofIssue": "24 Apr 2024",
            "DueDate": "20 May 2024",
            "IssueTo": "Joann",
            "Class":"IV, B",
            "BooksIssued": "5",
            "BookReturned": "3",
            "Image": "assets/img/students/student-02.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853627",
            "DateofIssue": "02 May 2024",
            "DueDate": "01 Jun 2024",
            "IssueTo": "Kathleen",
            "Class": "III, A",
            "BooksIssued": "4",
            "BookReturned": "2",
            "Image": "assets/img/students/student-03.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853626",
            "DateofIssue": "16 May 2024",
            "DueDate": "15 Jun 2024",
            "IssueTo": "Gifford",
            "Class":"I, B",
            "BooksIssued": "3",
            "BookReturned": "2",
            "Image": "assets/img/students/student-04.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853625",
            "DateofIssue": "22 May 2024",
            "DueDate": "20 Jun 2024",
            "IssueTo": "Lisa",
            "Class":"II, B",
            "BooksIssued": "6",
            "BookReturned": "4",
            "Image": "assets/img/students/student-05.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853624",
            "DateofIssue": "10 Jun 2024",
            "DueDate": "08 Jul 2024",
            "IssueTo": "Ralph",
            "Class":"III, B",
            "BooksIssued": "4",
            "BookReturned": "2",
            "Image": "assets/img/students/student-06.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853623",
            "DateofIssue": "15 Jun 2024",
            "DueDate": "14 Jul 2024",
            "IssueTo": "Julie",
            "Class":"V, A",
            "BooksIssued": "5",
            "BookReturned": "3",
            "Image": "assets/img/students/student-07.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853622",
            "DateofIssue": "26 Jun 2024",
            "DueDate": "25 Jul 2024",
            "IssueTo": "Ryan",
            "Class":"VI, A",
            "BooksIssued": "3",
            "BookReturned": "1",
            "Image": "assets/img/students/student-08.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853621",
            "DateofIssue": "06 Jul 2024",
            "DueDate": "05 Aug 2024",
            "IssueTo": "Susan",
            "Class":"VIII, B",
            "BooksIssued": "6",
            "BookReturned": "4",
            "Image": "assets/img/students/student-09.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853620",
            "DateofIssue": "18 Jul 2024",
            "DueDate": "16 Aug 2024",
            "IssueTo": "Richard",
            "Class":"VII, B",
            "BooksIssued": "2",
            "BookReturned": "1",
            "Image": "assets/img/students/student-10.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
]
    return render(request, 'pages/management/library/library-issue-book.html', {'library_issue_book' : library_issue_book})
    
def library_return(request):
    library_return = [
        {
            "ID": "IB853629",
            "DateofIssue": "20 Apr 2024",
            "DueDate": "19 May 2024",
            "IssueTo": "Janet",
            "Class":"III, A",
            "BooksIssued": "1",
            "BookReturned": "0",
            "Image": "assets/img/students/student-01.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853628",
            "DateofIssue": "24 Apr 2024",
            "DueDate": "20 May 2024",
            "IssueTo": "Joann",
            "Class":"IV, B",
            "BooksIssued": "5",
            "BookReturned": "3",
            "Image": "assets/img/students/student-02.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853627",
            "DateofIssue": "02 May 2024",
            "DueDate": "01 Jun 2024",
            "IssueTo": "Kathleen",
            "Class": "III, A",
            "BooksIssued": "4",
            "BookReturned": "2",
            "Image": "assets/img/students/student-03.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853626",
            "DateofIssue": "16 May 2024",
            "DueDate": "15 Jun 2024",
            "IssueTo": "Gifford",
            "Class":"I, B",
            "BooksIssued": "3",
            "BookReturned": "2",
            "Image": "assets/img/students/student-04.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853625",
            "DateofIssue": "22 May 2024",
            "DueDate": "20 Jun 2024",
            "IssueTo": "Lisa",
            "Class":"II, B",
            "BooksIssued": "6",
            "BookReturned": "4",
            "Image": "assets/img/students/student-05.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853624",
            "DateofIssue": "10 Jun 2024",
            "DueDate": "08 Jul 2024",
            "IssueTo": "Ralph",
            "Class":"III, B",
            "BooksIssued": "4",
            "BookReturned": "2",
            "Image": "assets/img/students/student-06.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853623",
            "DateofIssue": "15 Jun 2024",
            "DueDate": "14 Jul 2024",
            "IssueTo": "Julie",
            "Class":"V, A",
            "BooksIssued": "5",
            "BookReturned": "3",
            "Image": "assets/img/students/student-07.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853622",
            "DateofIssue": "26 Jun 2024",
            "DueDate": "25 Jul 2024",
            "IssueTo": "Ryan",
            "Class":"VI, A",
            "BooksIssued": "3",
            "BookReturned": "1",
            "Image": "assets/img/students/student-08.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853621",
            "DateofIssue": "06 Jul 2024",
            "DueDate": "05 Aug 2024",
            "IssueTo": "Susan",
            "Class":"VIII, B",
            "BooksIssued": "6",
            "BookReturned": "4",
            "Image": "assets/img/students/student-09.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
        {
            "ID": "IB853620",
            "DateofIssue": "18 Jul 2024",
            "DueDate": "16 Aug 2024",
            "IssueTo": "Richard",
            "Class":"VII, B",
            "BooksIssued": "2",
            "BookReturned": "1",
            "Image": "assets/img/students/student-10.jpg",
            "IssueRemarks": "Book Issued",
            "Action": "View Details",
        },
    ]
    return render(request, 'pages/management/library/library-return.html', {'library_return' : library_return})

def sports(request):
    sports = [
        {
            "ID": "SP826329",
            "Name": "Cricket",
            "Coach": "Thomas",
            "Image": "assets/img/coach/coach-01.jpg",
            "StartedYear": "2004",
        },
        {
            "ID": "SP826328",
            "Name": "Throwball",
            "Coach": "Georgia",
            "Image": "assets/img/coach/coach-02.jpg",
            "StartedYear": "2005",
        },
        {
            "ID": "SP826327",
            "Name": "Football",
            "Coach": "Nicholas",
            "Image": "assets/img/coach/coach-03.jpg",
            "StartedYear": "2006",
        },
        {
            "ID": "SP826326",
            "Name": "Tennis",
            "Coach": "Sandra",
            "Image": "assets/img/coach/coach-04.jpg",
            "StartedYear": "2007",
        },
        {
            "ID": "SP826325",
            "Name": "Basketball",
            "Coach": "Jon",
            "Image": "assets/img/coach/coach-05.jpg",
            "StartedYear": "2008",
        },
        {
            "ID": "SP826324",
            "Name": "Badminton",
            "Coach": "Shannon",
            "Image": "assets/img/coach/coach-06.jpg",
            "StartedYear": "2009",
        },
        {
            "ID": "SP826323",
            "Name": "Carrom",
            "Coach": "Wilson",
            "Image": "assets/img/coach/coach-07.jpg",
            "StartedYear": "2010",
        },
        {
            "ID": "SP826322",
            "Name": "Chess",
            "Coach": "Sonia",
            "Image": "assets/img/coach/coach-08.jpg",
            "StartedYear": "2011",
        },
        {
            "ID": "SP826321",
            "Name": "Volleyball",
            "Coach": "Adams",
            "Image": "assets/img/coach/coach-09.jpg",
            "StartedYear": "2012",
        },
        {
            "ID": "SP826320",
            "Name": "Hockey",
            "Coach": "Lydia",
            "Image": "assets/img/coach/coach-10.jpg",
            "StartedYear": "2013",
        },
        ]
    return render(request, 'pages/management/sports.html', {'sports' : sports})

def players(request):
    players = [
        {
            "ID": "SP826329",
            "PlayerName": "Francis",
            "Image": "assets/img/players/player-01.jpg",
            "Sports": "Cricket",
            "DateofJoin": "25 Apr 2024",
        },
        {
            "ID": "SP826328",
            "PlayerName": "Cheryl",
            "Image": "assets/img/players/player-02.jpg",
            "Sports": "Throwball",
            "DateofJoin": "28 Apr 2024",
        },
        {
            "ID": "SP826327",
            "PlayerName": "Daniel",
            "Image": "assets/img/players/player-03.jpg",
            "Sports": "Football",
            "DateofJoin": "04 May 2024",
        },
        {
            "ID": "SP826326",
            "PlayerName": "Irene",
            "Image": "assets/img/players/player-04.jpg",
            "Sports": "Tennis",
            "DateofJoin": "16 May 2024",
        },
        {
            "ID": "SP826325",
            "PlayerName": "Keith",
            "Image": "assets/img/players/player-05.jpg",
            "Sports": "Basketball",
            "DateofJoin": "20 May 2024",
        },
        {
            "ID": "SP826324",
            "PlayerName": "Dina",
            "Image": "assets/img/players/player-06.jpg",
            "Sports": "Badminton",
            "DateofJoin": "12 Jun 2024",
        },
        {
            "ID": "SP826323",
            "PlayerName": "Michael",
            "Image": "assets/img/players/player-07.jpg",
            "Sports": "Carrom",
            "DateofJoin": "17 Jun 2024",
        },
        {
            "ID": "SP826322",
            "PlayerName": "Julia",
            "Image": "assets/img/players/player-08.jpg",
            "Sports": "Chess",
            "DateofJoin": "27 Jun 2024",
        },
        {
            "ID": "SP826321",
            "PlayerName": "Ray",
            "Image": "assets/img/players/player-09.jpg",
            "Sports": "Hockey",
            "DateofJoin": "10 Jul 2024",
        },
        {
            "ID": "SP826320",
            "PlayerName": "Lois",
            "Image": "assets/img/players/player-10.jpg",
            "Sports": "Volleyball",
            "DateofJoin": "20 Jul 2024",
        },
        ]
    return render(request, 'pages/management/players.html', {'players' : players})

def hostel_list(request):
    hostel_list = [
        {
            "ID": "H823828",
            "HostelName": "Phoenix Residence",
            "HostelType": "Boys",
            "Address": "25 Crowfield Road, Phoenix",
            "InTake": "150",
            "Description": "Rising to nurture young minds",
        },
        {
            "ID": "H823827",
            "HostelName": "Tranquil Haven",
            "HostelType": "Girls",
            "Address": "81 Hartland Avenue, Milwaukee",
            "InTake": "200",
            "Description": "Rising to nurture young minds",
        },
        {
            "ID": "H823826",
            "HostelName": "Radiant Towers",
            "HostelType": "Boys",
            "Address": "School Campus",
            "InTake": "180",
            "Description": "Illuminating minds with knowledge and warmth",
        },
        {
            "ID": "H823825",
            "HostelName": "Nova Nest",
            "HostelType": "Girls",
            "Address": "School Campus",
            "InTake": "180",
            "Description": "A nestling ground for budding intellectuals to thrive",
        },
        {
            "ID": "H823824",
            "HostelName": "Vista Villat",
            "HostelType": "Boys",
            "Address": "65 Braxton Street, Sheffield",
            "InTake": "250",
            "Description": "Overlooking the vast landscape of knowledge",
        },
        {
            "ID": "H823823",
            "HostelName": "Zenith Zone",
            "HostelType": "Girls",
            "Address": "School Campus",
            "InTake": "150",
            "Description": "Living at the peak of academic achievement",
        },
        {
            "ID": "H823822",
            "HostelName": "Summit Springs",
            "HostelType": "Boys",
            "Address": "55 Upton Avenue, Monson",
            "InTake": "300",
            "Description": "Drawing from the wellspring of knowledge",
        },
        {
            "ID": "H823821",
            "HostelName": "Beacon Breeze",
            "HostelType": "Girls",
            "Address": "School Campus",
            "InTake": "280",
            "Description": "Riding the winds of educational inspiration",
        },
        {
            "ID": "H823820",
            "HostelName": "Empyrean Estate",
            "HostelType": "Boys",
            "Address": "45 Cinnamon Lane, San Antonio",
            "InTake": "200",
            "Description": "Infusing energy into scholarly endeavors",
        },
        {
            "ID": "H823819",
            "HostelName": "Nexus Nook",
            "HostelType": "Girls",
            "Address": "School Campus",
            "InTake": "350",
            "Description": "A communal hub for academic excellence",
        },
        ]
    return render(request, 'pages/management/hostel/hostel-list.html',{'hostel_list' : hostel_list})

def hostel_rooms(request):
    hostel_rooms = [
        {
            "ID": "HR819382",
            "RoomNo": "A1",
            "HostelName": "Phoenix Residence",
            "RoomType": "One Bed",
            "NoofBed": "1",
            "CostperBed": "$200",
        },
        {
            "ID": "HR819381",
            "RoomNo": "A2",
            "HostelName": "Tranquil Haven",
            "RoomType": "One Bed AC",
            "NoofBed": "1",
            "CostperBed": "$300",
        },
        {
            "ID": "HR819380",
            "RoomNo": "A3",
            "HostelName": "Radiant Towers",
            "RoomType": "Two Bed",
            "NoofBed": "2",
            "CostperBed": "$400",
        },
        {
            "ID": "HR819379",
            "RoomNo": "A4",
            "HostelName": "Nova Nest",
            "RoomType": "One Bed",
            "NoofBed": "1",
            "CostperBed": "$200",
        },
        {
            "ID": "HR819378",
            "RoomNo": "B1",
            "HostelName": "Vista Villa",
            "RoomType": "One Bed AC",
            "NoofBed": "1",
            "CostperBed": "$300",
        },
        {
            "ID": "HR819377",
            "RoomNo": "B2",
            "HostelName": "Zenith Zone",
            "RoomType": "Two Bed",
            "NoofBed": "2",
            "CostperBed": "$400",
        },
        {
            "ID": "HR819376",
            "RoomNo": "B3",
            "HostelName": "Summit Springs",
            "RoomType": "One Bed",
            "NoofBed": "1",
            "CostperBed": "$200e",
        },
        {
            "ID": "HR819375",
            "RoomNo": "B4",
            "HostelName": "Beacon Breeze",
            "RoomType": "Two Bed AC",
            "NoofBed": "2",
            "CostperBed": "$600",
        },
        {
            "ID": "HR819374",
            "RoomNo": "C1",
            "HostelName": "Empyrean Estate",
            "RoomType": "One Bed",
            "NoofBed": "1",
            "CostperBed": "$200",
        },
        {
            "ID": "HR819373",
            "RoomNo": "C2",
            "HostelName": "Nexus Nook",
            "RoomType": "Two Bed AC",
            "NoofBed": "2",
            "CostperBed": "$600",
        },
    ]
    return render(request, 'pages/management/hostel/hostel-rooms.html',{'hostel_rooms' : hostel_rooms})

def hostel_room_type(request):
    hostel_room_type = [
        {
            "ID": "RT846235",
            "RoomType": "One Bed",
            "Description":
            "Enjoy serene solitude in our one-bed room, your tranquil retreat for focused studying",
        },
        {
            "ID": "RT846234",
            "RoomType": "One Bed AC",
            "Description": "Stay cool and focused in our one-bed AC room, your serene study haven",
        },
        {
            "ID": "RT846233",
            "RoomType": "Two Bed",
            "Description": "Study together in comfort and camaraderie in our two-bed room",
        },
        {
            "ID": "RT846232",
            "RoomType": "Two Bed AC",
            "Description": "Stay cool and study together in comfort in our two-bed AC room",
        },
        {
            "ID": "RT846231",
            "RoomType": "Three Bed",
            "Description":
            "Study comfortably in our spacious three-bed room, share learning and camaraderie",
        },
        {
            "ID": "RT846230",
            "RoomType": "Three Bed AC",
            "Description":
            "Experience collaborative studying in comfort with our three-bed AC room",
        },
        {
            "ID": "RT846229",
            "RoomType": "Four Bed",
            "Description":
            "Engage in group study sessions and foster camaraderie in our spacious four-bed room",
        },
        {
            "ID": "RT846228",
            "RoomType": "Four Bed AC",
            "Description":
            "Experience collaborative study sessions in comfort with our spacious four-bed AC room",
        },
        {
            "ID": "RT846227",
            "RoomType": "Five Bed",
            "Description": "Foster teamwork and academic synergy, ideal for group study sessions",
        },
        {
            "ID": "RT846226",
            "RoomType": "Five Bed AC",
            "Description":
            "Optimal comfort meets collaborative studying, perfect for academic synergy among residents.",
        },
        ]
    return render(request, 'pages/management/hostel/hostel-room-type.html',{'hostel_room_type' : hostel_room_type})

def transport_routes(request):
    transport_routes = [
        {
            "ID": "R124556",
            "Routes": "Seattle",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "15 May 2024",
        },
        {
            "ID": "R124555",
            "Routes": "Brooklyn Central",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "14 May 2024",
        },
        {
            "ID": "R124554",
            "Routes": "Rochester",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "13 May 2024",
        },
        {
            "ID": "R124553",
            "Routes": "Kansas City",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "12 May 2024",
        },
        {
            "ID": "RR124552",
            "Routes": "Brooklyn North",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "11 May 2024",
        },
        {
            "ID": "RR124551",
            "Routes": "Port Graham",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "10 May 2024",
        },
        {
            "ID": "R24550",
            "Routes": "Nashville",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "09 May 2024",
        },
        {
            "ID": "R24549",
            "Routes": "Detroit",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
            "AddedOn": "08 May 2024",
        },
        {
            "ID": "R124548",
            "Routes": "Camden",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "07 May 2024",
        },
        {
            "ID": "R124547",
            "Routes": "Terra Bella",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "07 May 2024",
        },
        ]
    return render(request, 'pages/management/transport/transport-routes.html',{'transport_routes' : transport_routes})

def transport_pickup_points(request):
    transport_pickup_points = [
        {    
            "ID": "PP124556",
            "PickupPoint": "2603 Wood Duck Drive Marquette, MI",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "15 May 2024",
        },
        {    
            "ID": "PP124555",
            "PickupPoint": "3521 Harvest Lane Kansas City, MO",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "14 May 2024",
        },
        {    
            "ID": "PP124554",
            "PickupPoint": "4025 Khale Street, Folly Beach, SC",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "13 May 2024",
        },
        {    
            "ID": "PP124553",
            "PickupPoint": "2261 Sweetwood Drive, Denver, CO",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "12 May 2024",
        },
        {    
            "ID": "PP124552",
            "PickupPoint": "3341 Palmer Road, Columbus, OH",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "11 May 2024",
        },
        {    
            "ID": "PP124551",
            "PickupPoint": "1609 Smith Street, Worcester, MA",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "10 May 2024",
        },
        {    
            "ID": "PP24550",
            "PickupPoint": "3167 Stadium Drive, Worcester, MA",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "09 May 2024",
        },
        {    
            "ID": "PP24549",
            "PickupPoint": "4650 Aviation Way, Los Angeles, CA",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
            "AddedOn": "08 May 2024",
        },
        {
            "ID": "PP124548",
            "PickupPoint": "2693 Parker Drive, Cleveland, OH",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "07 May 2024",
        },
        {
            "ID": "PP124547",
            "PickupPoint": "2233 Wood Street, Slidell, LA",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "AddedOn": "07 May 2024",
        },
]
    return render(request, 'pages/management/transport/transport-pickup-points.html',{'transport_pickup_points' : transport_pickup_points})
    
def transport_vehicle_drivers(request):
    transport_vehicle_drivers = [
        {
            "ID": "D0482",
            "Driver": "Mary",
            "PhoneNumber": "+1 64044 74890",
            "DriverLicenseNo": "LC7899456689",
            "Address": "2233 Wood Street, Slidell, LA",
            "Status": "Active",
            "Image": "assets/img/parents/parent-10.jpg",
        },
        {
            "ID": "D0481",
            "Driver": "Thomas" ,
            "PhoneNumber": "+1 14541 55665",
            "DriverLicenseNo": "LCS4579454785",
            "Address": "2693 Parker Drive, Cleveland, OH",
            "Status": "Active",
            "Image": "assets/img/parents/parent-01.jpg",
        },
        {
            "ID": "D0480",
            "Driver": "Michael",
            "PhoneNumber": "+1 78954 85461",
            "DriverLicenseNo": "LCS3254789541",
            "Address": "4650 Aviation Way, Los Angeles, CA",
            "Status": "Active",
            "Image": "assets/img/parents/parent-09.jpg",
        },
        {
            "ID": "D0479",
            "Driver": "Jessie",
            "PhoneNumber": "+1 12345 68891",
            "DriverLicenseNo": "LCS1478545214",
            "Address": "3167 Stadium Drive, Worcester, MA",
            "Status": "Active",
            "Image": "assets/img/parents/parent-08.jpg",
        },
        {
            "ID": "D0478",
            "Driver": "Robert",
            "PhoneNumber": "+1 78454 7884",
            "DriverLicenseNo": "LCS6985478541",
            "Address": "1609 Smith Street, Worcester, MA",
            "Status": "Active",
            "Image": "assets/img/parents/parent-07.jpg",
        },
        {
            "ID": "D0477",
            "Driver": "Colleen",
            "PhoneNumber": "+1 78546 97894",
            "DriverLicenseNo": "LCS3254145874",
            "Address": "3341 Palmer Road, Columbus, OH",
            "Status": "Active",
            "Image": "assets/img/parents/parent-06.jpg",
        },
        {
            "ID": "D0476",
            "Driver": "Arthur",
            "PhoneNumber": "+1 97878 87854",
            "DriverLicenseNo": "LCS4854651254",
            "Address": "2261 Sweetwood Drive, Denver, CO",
            "Status": "Active",
            "Image": "assets/img/parents/parent-05.jpg",
        },
        {
            "ID": "D0475",
            "Driver": "Claudia",
            "PhoneNumber": "+1 64599 78542",
            "DriverLicenseNo": "LCS9658745214",
            "Address": "4025 Khale Street, Folly Beach, SC",
            "Status": "Inactive",
            "Image": "assets/img/parents/parent-04.jpg",
        },
        {
            "ID": "D0474",
            "Driver": "Johnson",
            "PhoneNumber": "+1 45781 45145",
            "DriverLicenseNo": "LCS7854652145",
            "Address": "3521 Harvest Lane Kansas City, MO",
            "Status": "Active",
            "Image": "assets/img/parents/parent-03.jpg",
        },
        {
            "ID": "D0473",
            "Driver": "Marquita",
            "PhoneNumber": "+1 45112 48879",
            "DriverLicenseNo": "LCS9985231258",
            "Address": "2603 Wood Duck Drive Marquette, MI",
            "Status": "Active",
            "Image": "assets/img/parents/parent-02.jpg",
        },
]
    return render(request, 'pages/management/transport/transport-vehicle-drivers.html',{'transport_vehicle_drivers' : transport_vehicle_drivers})
        
def transport_vehicle(request):
    transport_vehicle = [
        {
            "ID": "B80482",
            "VehicleNo": "8930",
            "VehicleModel": "Scania",
            "Image": "assets/img/parents/parent-01.jpg",
            "MadeofYear": "2021",
            "RegistrationNo": "US1A3545",
            "ChassisNo": "32546665456",
            "GPSDeviceID": "GPS7899456689",
            "Live": "Live Track",
            "Driver": "Thomas",
            "Phone": "+1 64044 748904",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "VehicleNo": "1235",
            "VehicleModel": "Mini Bus",
            "Image": "assets/img/parents/parent-10.jpg",
            "MadeofYear": "2024",
            "RegistrationNo": "US2B5465",
            "ChassisNo": "12345678901",
            "GPSDeviceID": "GPS4579454785",
            "Live": "Live Track",
            "Driver": "Mary",
            "Phone": "+1 14541 55665",
            "Status": "Active",
        },
        {
            "ID": "B80482",
            "VehicleNo": "6465",
            "VehicleModel": "Mini Bus",
            "Image": "assets/img/parents/parent-09.jpg",
            "MadeofYear": "2017",
            "RegistrationNo": "US3C4547",
            "ChassisNo": "22124413454",
            "GPSDeviceID": "GPS3254789541",
            "Live": "Live Track",
            "Driver": "Michael",
            "Phone": "+1 78954 85461",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "VehicleNo": "7895",
            "VehicleModel": "Kinsmart",
            "Image": "assets/img/parents/parent-08.jpg",
            "MadeofYear": "2022",
            "RegistrationNo": "US4D1234",
            "ChassisNo": "12516665456",
            "GPSDeviceID": "GPS1478545214",
            "Live": "Live Track",
            "Driver": "Jessie",
            "Phone": "+1 12345 68891",
            "Status": "Active",
        },
        {
            "ID": "B80482",
            "VehicleNo": "4625",
            "VehicleModel": "Kinsmart",
            "Image": "assets/img/parents/parent-07.jpg",
            "MadeofYear": "2019",
            "RegistrationNo": "US1A6547",
            "ChassisNo": "22746675177",
            "GPSDeviceID": "GPS6985478541",
            "Live": "Live Track",
            "Driver": "Robert",
            "Phone": "+1 78454 78841",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "VehicleNo": "7854",
            "VehicleModel": "Single deck",
            "Image": "assets/img/parents/parent-06.jpg",
            "MadeofYear": "2015",
            "RegistrationNo": "US2B5977",
            "ChassisNo": "32546665456",
            "GPSDeviceID": "GPS3254145874",
            "Live": "Live Track",
            "Driver": "Colleen",
            "Phone": "+1 78546 97894",
            "Status": "Active",
        },
        {
            "ID": "B80482",
            "VehicleNo": "9789",
            "VehicleModel": "Kinsmart",
            "Image": "assets/img/parents/parent-05.jpg",
            "MadeofYear": "2024",
            "RegistrationNo": "US1A3147",
            "ChassisNo": "16546647421",
            "GPSDeviceID": "GPS4854651254",
            "Live": "Live Track",
            "Driver": "Arthur",
            "Phone": "+1 97878 87854",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "VehicleNo": "4569",
            "VehicleModel": "Mini Bus",
            "Image": "assets/img/parents/parent-04.jpg",
            "MadeofYear": "2016",
            "RegistrationNo": "US2B5789",
            "ChassisNo": "75546785147",
            "GPSDeviceID": "GPS9658745214",
            "Live": "Live Track",
            "Driver": "Claudia",
            "Phone": "+1 64599 78542",
            "Status": "Inactive",
        },
        {
            "ID": "B80482",
            "VehicleNo": "7857",
            "VehicleModel": "Mini Bus",
            "Image": "assets/img/parents/parent-03.jpg",
            "MadeofYear": "2018",
            "RegistrationNo": "US1A3147",
            "ChassisNo": "32546647992",
            "GPSDeviceID": "GPS7854652145",
            "Live": "Live Track",
            "Driver": "Johnson",
            "Phone": "+1 45781 45145",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "VehicleNo": "6879",
            "VehicleModel": "Single deck",
            "Image": "assets/img/parents/parent-02.jpg",
            "MadeofYear": "2023",
            "RegistrationNo": "US2B5244",
            "ChassisNo": "14578665456",
            "GPSDeviceID": "GPS9985231258",
            "Live": "Live Track",
            "Driver": "Marquita",
            "Phone": "+1 45112 48879",
            "Status": "Active",
        },
]
    return render(request, 'pages/management/transport/transport-vehicle.html',{'transport_vehicle' : transport_vehicle})

def transport_assign_vehicle(request):
    transport_assign_vehicle = [
        {
            "ID": "B80482",
            "Route": "Seattle",
            "PickupPoint": "2233 Wood Street, Slidell, LA",
            "Vehicle": "8930",
            "Driver": "Thomas",
            "Image": "assets/img/parents/parent-01.jpg",
            "Phone": "+1 64044 748904",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "B80481",
            "Route": "Camden",
            "PickupPoint": "2693 Parker Drive, Cleveland, OH",
            "Vehicle": "1235",
            "Driver": "Mary",
            "Image": "assets/img/parents/parent-10.jpg",
            "Phone": "+1 14541 55665",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
        },
        {
            "ID": "B80482",
            "Route": "Detroit",
            "PickupPoint": "4650 Aviation Way, Los Angeles, CA",
            "Vehicle": "6465",
            "Driver": "Michael",
            "Image": "assets/img/parents/parent-09.jpg",
            "Phone": "+1 78954 85461",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "Route": "Nashville",
            "PickupPoint": "3167 Stadium Drive, Worcester, MA",
            "Vehicle": "7895",
            "Driver": "Jessie",
            "Image": "assets/img/parents/parent-08.jpg",
            "Phone": "+1 12345 68891",
            "Status": "Active",
        },
        {
            "ID": "B80482",
            "Route": "Port Graham",
            "PickupPoint": "1609 Smith Street, Worcester, MA",
            "Vehicle": "4625",
            "Driver": "Robert",
            "Image": "assets/img/parents/parent-07.jpg",
            "Phone": "+1 78454 78841",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "Route": "Brooklyn North",
            "PickupPoint": "3341 Palmer Road, Columbus, OH",
            "Vehicle": "7854",
            "Driver": "Colleen",
            "Image": "assets/img/parents/parent-06.jpg",
            "Phone": "+1 78546 97894",
            "Status": "Active",
        },
        {
            "ID": "B80482",
            "Route": "Kansas City",
            "PickupPoint": "2261 Sweetwood Drive, Denver, CO",
            "Vehicle": "9789",
            "Driver": "Arthur",
            "Image": "assets/img/parents/parent-05.jpg",
            "Phone": "+1 97878 87854",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "Route": "Rochester",
            "PickupPoint": "4025 Khale Street, Folly Beach, SC",
            "Vehicle": "4569",
            "Driver": "Claudia",
            "Image": "assets/img/parents/parent-04.jpg",
            "Phone": "+1 64599 78542",
            "Status": "Inactive",
        },
        {
            "ID": "B80482",
            "Route": "Brooklyn Central",
            "PickupPoint": "3521 Harvest Lane Kansas City, MO",
            "Vehicle": "7857",
            "Driver": "Johnson",
            "Image": "assets/img/parents/parent-03.jpg",
            "Phone": "+1 45781 45145",
            "Status": "Active",
        },
        {
            "ID": "B80481",
            "Route": "Seattle",
            "PickupPoint": "2603 Wood Duck Drive Marquette, MI",
            "Vehicle": "6879",
            "Driver": "Marquita",
            "Image": "assets/img/parents/parent-02.jpg",
            "Phone": "+1 45112 48879",
            "Status": "Active",
        },
]
    return render(request, 'pages/management/transport/transport-assign-vehicle.html',{'transport_assign_vehicle' : transport_assign_vehicle})

#UI Module

def ui_alerts(request):
    return render(request, 'pages/uiinterface/baseui/ui-alerts.html')
 
def ui_accordion(request):
    return render(request, 'pages/uiinterface/baseui/ui-accordion.html')
 
def ui_avatar(request):
    return render(request, 'pages/uiinterface/baseui/ui-avatar.html')
 
def ui_badges(request):
    return render(request, 'pages/uiinterface/baseui/ui-badges.html')
 
def ui_borders(request):
    return render(request, 'pages/uiinterface/baseui/ui-borders.html')
 
def ui_buttons(request):
    return render(request, 'pages/uiinterface/baseui/ui-buttons.html')
 
def ui_buttons_group(request):
    return render(request, 'pages/uiinterface/baseui/ui-buttons-group.html')
 
def ui_breadcrumb(request):
    return render(request, 'pages/uiinterface/baseui/ui-breadcrumb.html')
 
def ui_cards(request):
    return render(request, 'pages/uiinterface/baseui/ui-cards.html')
 
def ui_carousel(request):
    return render(request, 'pages/uiinterface/baseui/ui-carousel.html')
 
def ui_colors(request):
    return render(request, 'pages/uiinterface/baseui/ui-colors.html')
 
def ui_dropdowns(request):
    return render(request, 'pages/uiinterface/baseui/ui-dropdowns.html')
 
def ui_grid(request):
    return render(request, 'pages/uiinterface/baseui/ui-grid.html')
 
def ui_images(request):
    return render(request, 'pages/uiinterface/baseui/ui-images.html')
 
def ui_lightbox(request):
    return render(request, 'pages/uiinterface/baseui/ui-lightbox.html')
 
def ui_media(request):
    return render(request, 'pages/uiinterface/baseui/ui-media.html')
 
def ui_modals(request):
    return render(request, 'pages/uiinterface/baseui/ui-modals.html')
 
def ui_offcanvas(request):
    return render(request, 'pages/uiinterface/baseui/ui-offcanvas.html')
 
def ui_pagination(request):
    return render(request, 'pages/uiinterface/baseui/ui-pagination.html')
 
def ui_popovers(request):
    return render(request, 'pages/uiinterface/baseui/ui-popovers.html')
 
def ui_progress(request):
    return render(request, 'pages/uiinterface/baseui/ui-progress.html')
 
def ui_placeholders(request):
    return render(request, 'pages/uiinterface/baseui/ui-placeholders.html')
 
def ui_spinner(request):
    return render(request, 'pages/uiinterface/baseui/ui-spinner.html')
 
def ui_sweetalerts(request):
    return render(request, 'pages/uiinterface/baseui/ui-sweetalerts.html')
 
def ui_nav_tabs(request):
    return render(request, 'pages/uiinterface/baseui/ui-nav-tabs.html')
 
def ui_toasts(request):
    return render(request, 'pages/uiinterface/baseui/ui-toasts.html')
 
def ui_tooltips(request):
    return render(request, 'pages/uiinterface/baseui/ui-tooltips.html')
 
def ui_typography(request):
    return render(request, 'pages/uiinterface/baseui/ui-typography.html')
 
def ui_video(request):
    return render(request, 'pages/uiinterface/baseui/ui-video.html')
 
#AdvancedUI 
 
def ui_ribbon(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-ribbon.html')
 
def ui_clipboard(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-clipboard.html')
 
def ui_drag_drop(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-drag-drop.html')
 
def ui_rangeslider(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-rangeslider.html')
 
def ui_rating(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-rating.html')
 
def ui_text_editor(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-text-editor.html')
 
def ui_counter(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-counter.html')
 
def ui_scrollbar(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-scrollbar.html')
 
def ui_stickynote(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-stickynote.html')
 
def ui_timeline(request):
    return render(request, 'pages/uiinterface/advanced-ui/ui-timeline.html')
 
#Charts

def chart_apex(request):
    return render(request, 'pages/uiinterface/charts/chart-apex.html')
 
def chart_c3(request):
    return render(request, 'pages/uiinterface/charts/chart-c3.html')
 
def chart_js(request):
    return render(request, 'pages/uiinterface/charts/chart-js.html')
 
def chart_morris(request):
    return render(request, 'pages/uiinterface/charts/chart-morris.html')
 
def chart_flot(request):
    return render(request, 'pages/uiinterface/charts/chart-flot.html')
 
def chart_peity(request):
    return render(request, 'pages/uiinterface/charts/chart-peity.html')
 
 
#Icons

def icon_fontawesome(request):
    return render(request, 'pages/uiinterface/icons/icon-fontawesome.html')
 
def icon_feather(request):
    return render(request, 'pages/uiinterface/icons/icon-feather.html')
 
def icon_ionic(request):
    return render(request, 'pages/uiinterface/icons/icon-ionic.html')
 
def icon_material(request):
    return render(request, 'pages/uiinterface/icons/icon-material.html')
 
def icon_pe7(request):
    return render(request, 'pages/uiinterface/icons/icon-pe7.html')
 
def icon_simpleline(request):
    return render(request, 'pages/uiinterface/icons/icon-simpleline.html')
 
def icon_themify(request):
    return render(request, 'pages/uiinterface/icons/icon-themify.html')

def icon_weather(request):
    return render(request, 'pages/uiinterface/icons/icon-weather.html')
 
def icon_typicon(request):
    return render(request, 'pages/uiinterface/icons/icon-typicon.html')
 
def icon_flag(request):
    return render(request, 'pages/uiinterface/icons/icon-flag.html')

#Forms
 
def form_basic_inputs(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-basic-inputs.html')
 
def form_checkbox_radios(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-checkbox-radios.html')
 
def form_input_groups(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-input-groups.html')
 
def form_grid_gutters(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-grid-gutters.html')
 
def form_select(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-select.html')
 
def form_mask(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-mask.html')
 
def form_fileupload(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-fileupload.html')
 
def form_elements(request):
    return render(request, 'pages/uiinterface/forms/form-elements/form-elements.html')
 
def form_horizontal(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-horizontal.html')
 
def form_vertical(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-vertical.html')
 
def form_floating_labels(request):
    return render(request, 'pages/uiinterface/forms/layouts/form-floating-labels.html')
 
def form_validation(request):
    return render(request, 'pages/uiinterface/forms/form-validation.html')
 
def form_select2(request):
    return render(request, 'pages/uiinterface/forms/form-select2.html')
 
def form_wizard(request):
    return render(request, 'pages/uiinterface/forms/form-wizard.html')

#Tables

def tables_basic(request):
    return render(request, 'pages/uiinterface/tables/tables-basic.html')
 
def data_tables(request):
    return render(request, 'pages/uiinterface/tables/data-tables.html')
 
#Support

def contact_messages(request):
    contact_messages = [
        {
            "ID": "CM482902",
            "Name": "Teresa",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Phone": "+1 82392 37359",
            "Email": "teresa@example.com",
            "Message": "Reminder: Staff meeting tomorrow.",
            "Date": "25 Mar 2024",
        },
        {
            "ID": "CM482901",
            "Name": "Hellana",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Phone": "+1 23566 52683",
            "Email": "hellena@example.com",
            "Message": "Sure, let's discuss it in class.",
            "Date": "14 Apr 2024",
        },
        {
            "ID": "CM482900",
            "Name": "William",
            "Image": "assets/img/users/user-27.jpg",
            "Phone": "+1 63792 50310",
            "Email": "william@example.com",
            "Message": "Requesting a meeting for next week.",
            "Date": "28 Apr 2024",
        },
        {
            "ID": "CM482899",
            "Name": "Daniel",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Phone": "+1 56752 86742",
            "Email": "daniel@example.com",
            "Message": "Meeting scheduled for June 10th.",
            "Date": "04 May 2024",
        },
        {
            "ID": "CM482898",
            "Name": "Galina",
            "Image": "assets/img/members/members-02.jpg",
            "Phone": "+1 91304 34834",
            "Email": "galina@example.com",
            "Message": "Reminder: Staff meeting tomorrow.",
            "Date": "17 May 2024",
        },
        {
            "ID": "CM482897",
            "Name": "Edward",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Phone": "+1 56187 87489",
            "Email": "edward@example.com",
            "Message": "Don't forget to submit the slip.",
            "Date": "20 May 2024",
        },
        {
            "ID": "CM482896",
            "Name": "Jacquelin",
            "Image": "assets/img/members/members-07.jpg",
            "Phone": "+1 77502 54845",
            "Email": "jacquelin@example.com",
            "Message": "Can we review the test tomorrow?",
            "Date": "03 Jun 2024",
        },
        {
            "ID": "CM482895",
            "Name": "Gary",
            "Image": "assets/img/users/user-09.jpg",
            "Phone": "+1 82239 42492",
            "Email": "gary@example.com",
            "Message": "Is there a summer camp program?",
            "Date": "15 Jun 2024",
        },
        {
            "ID": "CM482894",
            "Name": "Morgan",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Phone": "+1 63204 35730",
            "Email": "morgan@example.com",
            "Message": "Yes, registration starts next week.",
            "Date": "27 Jun 2024",
        },
        {
            "ID": "CM482893",
            "Name": "Aaron",
            "Image": "assets/img/teachers/teacher-06.jpg",
            "Phone": "+1 26267 80542",
            "Email": "aaron@example.com",
            "Message": "You have a missing assignment.",
            "Date": "10 Jul 2024",
        },
        ]
    return render(request, 'pages/support/contact-messages.html',{'contact_messages' : contact_messages})
 
def tickets(request):
    return render(request, 'pages/support/tickets.html')
  
def ticket_grid(request):
    return render(request, 'pages/support/ticket-grid.html') 
 
def ticket_details(request):
    return render(request, 'pages/support/ticket-details.html')
 
# Peoples

def student_grid(request):
    student_grid = [
        {
            "Img": "assets/img/students/student-01.jpg",
            "AdmissionNo": "AD9892434",
            "RollNo": "35013",
            "Name": "Janet  Daniel",
            "Class": "III, A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "10 Jan 2015",
        },
        {
            "Img": "assets/img/students/student-02.jpg",
            "AdmissionNo": "AD9892433",
            "RollNo": "35012",
            "Name": "Joann Michael",
            "Class": "IV, B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "19 Aug 2014",
        },
        {
            "Img": "assets/img/students/student-03.jpg",
            "AdmissionNo": "AD9892432",
            "RollNo": "35011",
            "Name": "Kathleen Dison",
            "Class": "III, A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "05 Dec 2017",
        },
        {
            "Img": "assets/img/students/student-04.jpg",
            "AdmissionNo": "AD9892431",
            "RollNo": "35010",
            "Name": "Lisa Gourley",
            "Class": "II, B",
            "Gender": "Female",
            "Status": "InActive",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "13 May 2017",
        },
        {
            "Img": "assets/img/students/student-05.jpg",
            "AdmissionNo": "AD9892430",
            "RollNo": "35009",
            "Name": "Ralph Claudia",
            "Class": "II, B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "20 Jun 2015",
        },
        {
            "Img": "assets/img/students/student-06.jpg",
            "AdmissionNo": "AD9892429",
            "RollNo": "35008",
            "Name": "Ralph Claudia",
            "Class": "III, B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "20 Jun 2015",
        },
        {
            "Img": "assets/img/students/student-06.jpg",
            "AdmissionNo": "AD9892428",
            "RollNo": "35007",
            "Name": "Julie Scott",
            "Class": "V, A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "18 Jan 2023",
        },
        {
            "Img": "assets/img/students/student-09.jpg",
            "AdmissionNo": "AD9892427",
            "RollNo": "35006",
            "Name": "Susan Boswell",
            "Class": "VIII, B",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "26 May 2020",
        },
        {
            "Img": "assets/img/students/student-08.jpg",
            "AdmissionNo": "AD9892426",
            "RollNo": "35005",
            "Name": "Richard Mayes",
            "Class": "V, A",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-danger",
            "DOB": "06 Oct 2022",
        },
        {
            "Img": "assets/img/students/student-12.jpg",
            "AdmissionNo": "AD9892425",
            "RollNo": "35004",
            "Name": "Richard Mayes",
            "Class": "VII, B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "06 Oct 2022",
        },
        {
            "Img": "assets/img/students/student-11.jpg",
            "AdmissionNo": "AD9892424",
            "RollNo": "35003",
            "Name": "Veronica Randle",
            "Class": "IX, A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "27 Dec 2009",
        },
        {
            "Img": "assets/img/students/student-10.jpg",
            "AdmissionNo": "AD9892423",
            "RollNo": "35002",
            "Name": "Thomas Hunt",
            "Class": "X, A",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "DOB": "11 Aug 2008",
        }
    ]
    return render(request, 'pages/peoples/students/student-grid.html',{'student_grid' : student_grid})

def student_list(request):
    student_lists = [
        {
            "Img": "assets/img/students/student-01.jpg",
            "AdmissionNo": "AD9892434",
            "RollNo": "35013",
            "Name": "Janet",
            "Class": "III",
            "Section": "A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "25 Mar 2024",
            "DOB": "10 Jan 2015",
        },
        {
            "Img": "assets/img/students/student-02.jpg",
            "AdmissionNo": "AD9892433",
            "RollNo": "35013",
            "Name": "Joann",
            "Class": "IV",
            "Section": "B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "18 Mar 2024",
            "DOB": "19 Aug 2014",
        },
        {
            "Img": "assets/img/students/student-03.jpg",
            "AdmissionNo": "AD9892432",
            "RollNo": "35011",
            "Name": "Kathleen",
            "Class": "II",
            "Section": "A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "14 Mar 2024",
            "DOB": "05 Dec 2017",
        },
        {
            "Img": "assets/img/students/student-04.jpg",
            "AdmissionNo": "AD9892431",
            "RollNo": "35010",
            "Name": "Gifford",
            "Class": "I",
            "Section": "B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "27 Feb 2024",
            "DOB": "22 Mar 2018",
        },
        {
            "Img": "assets/img/students/student-05.jpg",
            "AdmissionNo": "AD9892430",
            "RollNo": "35009",
            "Name": "Lisa",
            "Class": "II",
            "Section": "B",
            "Gender": "Female",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
            "DateofJoin": "13 Feb 2024",
            "DOB": "13 May 2017",
        },
        {
            "Img": "assets/img/students/student-06.jpg",
            "AdmissionNo": "AD9892429",
            "RollNo": "35008",
            "Name": "Ralph",
            "Class": "III",
            "Section": "B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "11 Feb 2024",
            "DOB": "20 Jun 2015",
        },
        {
            "Img": "assets/img/students/student-07.jpg",
            "AdmissionNo": "AD9892428",
            "RollNo": "35007",
            "Name": "Julie",
            "Class": "V",
            "Section": "A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "24 Jan 2024",
            "DOB": "18 Sep 2013",
        },
        {
            "Img": "assets/img/students/student-08.jpg",
            "AdmissionNo": "AD9892427",
            "RollNo": "35006",
            "Name": "Ryan",
            "Class": "VI",
            "Section": "A",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "19 Jan 2024",
            "DOB": "26 Nov 2012",
        },
        {
            "Img": "assets/img/students/student-09.jpg",
            "AdmissionNo": "AD9892426",
            "RollNo": "35005",
            "Name": "Susan",
            "Class": "VIII",
            "Section": "B",
            "Gender": "Female",
            "Status": "Inactive",
            "StatusClass": "badge badge-soft-danger",
            "DateofJoin": "08 Jan 2024",
            "DOB": "26 May 2010",
        },
        {
            "Img": "assets/img/students/student-10.jpg",
            "AdmissionNo": "AD9892425",
            "RollNo": "35004",
            "Name": "Richard",
            "Class": "VII",
            "Section": "B",
            "Gender": "Male",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "22 Dec 2024",
            "DOB": "06 Oct 2011",
        },
        {
            "Img": "assets/img/students/student-11.jpg",
            "AdmissionNo": "AD9892424",
            "RollNo": "35003",
            "Name": "Veronica",
            "Class": "IX",
            "Section": "A",
            "Gender": "Female",
            "Status": "Active",
            "StatusClass": "badge badge-soft-success",
            "DateofJoin": "15 Dec 2024",
            "DOB": "27 Dec 2009",
        }
    ]
    return render(request, 'pages/peoples/students/student-list.html', {'student_lists': student_lists})

def student_details(request):
    return render(request, 'pages/peoples/students/student-details/student-details.html')

def student_time_table(request):
    return render(request, 'pages/peoples/students/student-details/student-time-table.html')

def student_leaves(request):
    return render(request, 'pages/peoples/students/student-details/student-leaves.html')

def student_fees(request):
    return render(request, 'pages/peoples/students/student-details/student-fees.html')

def student_result(request):
    return render(request, 'pages/peoples/students/student-details/student-result.html')

def student_library(request):
    return render(request, 'pages/peoples/students/student-details/student-library.html')

def student_promotion(request):
    student_promotion = [
        {
            "Admission_No": "AD9892434",
            "Image": "assets/img/students/student-01.jpg",
            "Roll_No": "35013",
            "Name": "Janet",
            "Class": "III",
            "Section": "A",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892433",
            "Image": "assets/img/students/student-02.jpg",
            "Roll_No": "35013",
            "Name": "Joann",
            "Class": "IV",
            "Section": "B",
            'Exam_Result': "Pass",
        },
        {
            "Admission_No": "AD9892432",
            "Image": "assets/img/students/student-03.jpg",
            "Roll_No": "35011",
            "Name": "Kathleen",
            "Class": "II",
            "Section": "A",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892431",
            "Image": "assets/img/students/student-04.jpg",
            "Roll_No": "35010",
            "Name": "Gifford",
            "Class": "I",
            "Section": "B",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892430",
            "Image": "assets/img/students/student-05.jpg",
            "Roll_No": "35009",
            "Name": "Lisa",
            "Class": "II",
            "Section": "B",
            "Exam_Result": "Fail",
        },
        {
            "Admission_No": "AD9892429",
            "Image": "assets/img/students/student-06.jpg",
            "Roll_No": "35008",
            "Name": "Ralph",
            "Class": "III",
            "Section": "B",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892428",
            "Image": "assets/img/students/student-07.jpg",
            "Roll_No": "35007",
            "Name": "Julie",
            "Class": "V",
            "Section": "A",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892427",
            "Image": "assets/img/students/student-08.jpg",
            "Roll_No": "35006",
            "Name": "Ryan",
            "Class": "VI",
            "Section": "A",
            "Exam_Result": "Fail",
        },
        {
            "Admission_No": "AD9892426",
            "Image": "assets/img/students/student-09.jpg",
            "Roll_No": "35005",
            "Name": "Susan",
            "Class": "VIII",
            "Section": "B",
            "Exam_Result": "Fail",
        },
        {
            "Admission_No": "AD9892425",
            "Image": "assets/img/students/student-10.jpg",
            "Roll_No": "35004",
            "Name": "Richard",
            "Class": "VII",
            "Section": "B",
            "Exam_Result": "Pass",
        },
        {
            "Admission_No": "AD9892424",
            "Image": "assets/img/students/student-11.jpg",
            "Roll_No": "35003",
            "Name": "Veronica",
            "Class": "IX",
            "Section": "A",
            "Exam_Result": "Pass",
        },
]
    return render(request, 'pages/peoples/students/student-promotion.html', {'student_promotion': student_promotion})

def add_student(request):
    return render(request, 'pages/peoples/students/add-student.html')

def edit_student(request):
    return render(request, 'pages/peoples/students/edit-student.html')

def parent_grid(request):
    parent_grid = [
        {
            "ID": "P124556",
            "Name": "Thomas",
            "DateAdded": "25 Mar 2024",
            "Email": "tom@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-01.jpg",
            "ParentName": "Janet",
            "StudentImage": "assets/img/students/student-01.jpg"
        },
        {
            "ID": "P124555",
            "Name": "Marquita",
            "DateAdded": "18 Mar 2024",
            "Email": "mar@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-02.jpg",
            "ParentName": "Joann",
            "StudentImage": "assets/img/students/student-02.jpg"
        },
        {
            "ID": "P124554",
            "Name": "Johnson",
            "DateAdded": "14 Mar 2024",
            "Email": "joh@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-03.jpg",
            "ParentName": "Kathleen",
            "StudentImage": "assets/img/students/student-03.jpg"
        },
        {
            "ID": "P124552",
            "Name": "Arthur",
            "DateAdded": "11 Feb 2024",
            "Email": "art@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-05.jpg",
            "ParentName": "Gifford",
            "StudentImage": "assets/img/students/student-04.jpg"
        },
        {
            "ID": "P124551",
            "Name": "Colleen",
            "DateAdded": "24 Jan 2024",
            "Email": "col@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-06.jpg",
            "ParentName": "Lisa",
            "StudentImage": "assets/img/students/student-05.jpg"
        },
        {
            "ID": "P124550",
            "Name": "Robert",
            "DateAdded": "19 Jan 2024",
            "Email": "rob@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-07.jpg",
            "ParentName": "Ralph",
            "StudentImage": "assets/img/students/student-06.jpg"
        },
        {
            "ID": "P124548",
            "Name": "Michael",
            "DateAdded": "22 Dec 2023",
            "Email": "mic@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-09.jpg",
            "ParentName": "Julie",
            "StudentImage": "assets/img/students/student-07.jpg"
        },
        {
            "ID": "P124547",
            "Name": "Mary",
            "DateAdded": "15 Dec 2024",
            "Email": "mar@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-10.jpg",
            "ParentName": "Ryan",
            "StudentImage": "assets/img/students/student-08.jpg"
        },
        {
            "ID": "P124546",
            "Name": "Edwin",
            "DateAdded": "10 Dec 2023",
            "Email": "edw@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-11.jpg",
            "ParentName": "Susan",
            "StudentImage": "assets/img/students/student-09.jpg"
        },
        {
            "ID": "P124553",
            "Name": "Claudia",
            "DateAdded": "27 Feb 2024",
            "Email": "cla@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-04.jpg",
            "ParentName": "Richard",
            "StudentImage": "assets/img/students/student-09.jpg"
        },
        {
            "ID": "P124549",
            "Name": "Jessie",
            "DateAdded": "08 Jan 2024",
            "Email": "jes@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-08.jpg",
            "ParentName": "Kathleen",
            "StudentImage": "assets/img/students/student-03.jpg"
        },
        {
            "ID": "P124545",
            "Name": "Avila",
            "DateAdded": "01 Dec 2023",
            "Email": "avi@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-14.jpg",
            "ParentName": "Gifford",
            "StudentImage": "assets/img/students/student-04.jpg"
        }
    ]

    return render(request, 'pages/peoples/parents/parent-grid.html',{'parent_grid' : parent_grid})

def parent_list(request): 
    parent_list = [
        {
            "Image": "assets/img/parents/parent-01.jpg",
            "StudentImage" : "assets/img/students/student-01.jpg",
            "ID": "P124556",
            "ParentName": "Thomas",
            "Added" : "Added on 25 Mar 2024",
            "Child": "Janet",
            "Class" : "III, A",
            "Phone": "+1 65738 58937",
            "Email": "thomas@example.com",
        },
        {
            "Image": "assets/img/parents/parent-02.jpg",
            "StudentImage" : "assets/img/students/student-02.jpg",
            "ID": "P124555",
            "ParentName": "Marquita",
            "Added" : "Added on 18 Mar 2024",
            "Child": "Joann",
            "Class" : "IV, B",
            "Phone": "+1 47958 41398",
            "Email": "marquita@example.com",
        },
        {
            "Image": "assets/img/parents/parent-03.jpg",
            "StudentImage" : "assets/img/students/student-03.jpg",
            "ID": "P124554",
            "ParentName": "Johnson",
            "Added" : "Added on 14 Mar 2024",
            "Child": "Kathleen",
            "Class" : "III, A",
            "Phone": "+1 78688 17496",
            "Email": "johnson@example.com",
        },
        {
            "Image": "assets/img/parents/parent-04.jpg",
            "StudentImage" : "assets/img/students/student-04.jpg",
            "ID": "P124553",
            "ParentName": "Claudia",
            "Added" : "Added on 27 Feb 2024",
            "Child": "Gifford",
            "Class" : "I, B",
            "Phone": "+1 72323 05904",
            "Email": "claudia@example.com",
        },
        {
            "Image": "assets/img/parents/parent-05.jpg",
            "StudentImage" : "assets/img/students/student-05.jpg",
            "ID": "P124552",
            "ParentName": "Arthur",
            "Added" : "Added on 11 Feb 2024",
            "Child": "Lisa",
            "Class" : "II, B",
            "Phone": "+1 74820 48201",
            "Email": "arthur@example.com",
        },
        {
            "Image": "assets/img/parents/parent-06.jpg",
            "StudentImage" : "assets/img/students/student-06.jpg",
            "ID": "P124551",
            "ParentName": "Colleen",
            "Added" : "Added on 24 Jan 2024",
            "Child": "Ralph",
            "Class" : "III, B",
            "Phone": "+1 46169 47202",
            "Email": "colleen@example.com",
        },
        {
            "Image": "assets/img/parents/parent-07.jpg",
            "StudentImage" : "assets/img/students/student-07.jpg",
            "ID": "P124550",
            "ParentName": "Robert",
            "Added" : "Added on 19 Jan 2024",
            "Child": "Julie",
            "Class" : "V, A",
            "Phone": "+1 44990 27830",
            "Email": "robert@example.com",
        },
        {
            "Image": "assets/img/parents/parent-08.jpg",
            "StudentImage" : "assets/img/students/student-08.jpg",
            "ID": "P124549",
            "ParentName": "Jessie",
            "Added" : "Added on 08 Jan 2024",
            "Child": "Janet",
            "Class" : "III, A",
            "Phone": "+1 84634 04823",
            "Email": "jessie@example.com",
        },
        {
            "Image": "assets/img/parents/parent-09.jpg",
            "StudentImage" : "assets/img/students/student-09.jpg",
            "ID": "P124548",
            "ParentName": "Michael",
            "Added" : "Added on 22 Dec 2024",
            "Child": "Susan",
            "Class" : "VIII, B",
            "Phone": "+1 91038 68460",
            "Email": "michael@example.com",
        },
        {
            "Image": "assets/img/parents/parent-10.jpg",
            "StudentImage" : "assets/img/students/student-10.jpg",
            "ID": "P124547",
            "ParentName": "Mary",
            "Added" : "Added on 15 Dec 2024",
            "Child": "Richard",
            "Class" : "VII, B",
            "Phone": "+1 35835 71839",
            "Email": "mary@example.com",
        },
        {
            "Image": "assets/img/parents/parent-11.jpg",
            "StudentImage" : "assets/img/students/student-11.jpg",
            "ID": "P124546",
            "ParentName": "Edwin",
            "Added" : "Added on 10 Dec 2023",
            "Child": "Veronica",
            "Class" : "IX, A",
            "Phone": "+1 65738 58940",
            "Email": "edw@example.com",
        }
    ]
    return render(request, 'pages/peoples/parents/parent-list.html',{'parent_list' : parent_list})

def guardian_grid(request):
    guradian_grid = [
        {
            "ID": "G124545",
            "Name": "Avila",
            "AddedDate": "01 Dec 2023",
            "Email": "avi@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-12.jpg",
            "StudentName": "Janet",
            "StudentImage": "assets/img/students/student-04.jpg"
        },
        {
            "ID": "G124553",
            "Name": "Claudia",
            "AddedDate": "27 Feb 2024",
            "Email": "cla@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-04.jpg",
            "StudentName": "Richard",
            "StudentImage": "assets/img/students/student-12.jpg"
        },
        {
            "ID": "G124549",
            "Name": "Jessie",
            "AddedDate": "08 Jan 2024",
            "Email": "jes@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-08.jpg",
            "StudentName": "Kathleen",
            "StudentImage": "assets/img/students/student-03.jpg"
        },
        {
            "ID": "G124546",
            "Name": "Edwin",
            "AddedDate": "10 Dec 2023",
            "Email": "edw@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-11.jpg",
            "StudentName": "Susan",
            "StudentImage": "assets/img/students/student-09.jpg"
        },
        {
            "ID": "G124548",
            "Name": "Michael",
            "AddedDate": "22 Dec 2023",
            "Email": "mic@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-09.jpg",
            "StudentName": "Julie",
            "StudentImage": "assets/img/students/student-09.jpg"
        },
        {
            "ID": "G124547",
            "Name": "Mary",
            "AddedDate": "15 Dec 2024",
            "Email": "mar@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-10.jpg",
            "StudentName": "Ryan",
            "StudentImage": "assets/img/students/student-08.jpg"
        },
        {
            "ID": "G124550",
            "Name": "Robert",
            "AddedDate": "19 Jan 2024",
            "Email": "rob@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-07.jpg",
            "StudentName": "Ralph",
            "StudentImage": "assets/img/students/student-06.jpg"
        },
        {
            "ID": "G124551",
            "Name": "Colleen",
            "AddedDate": "24 Jan 2024",
            "Email": "col@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-06.jpg",
            "StudentName": "Lisa",
            "StudentImage": "assets/img/students/student-05.jpg"
        },
        {
            "ID": "G124556",
            "Name": "Thomas",
            "AddedDate": "25 Mar 2024",
            "Email": "tom@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-01.jpg",
            "StudentName": "Janet",
            "StudentImage": "assets/img/students/student-01.jpg"
        },
        {
            "ID": "G124554",
            "Name": "Johnson",
            "AddedDate": "14 Mar 2024",
            "Email": "joh@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-03.jpg",
            "StudentName": "Kathleen",
            "StudentImage": "assets/img/students/student-03.jpg"
        },
        {
            "ID": "G124555",
            "Name": "Marquita",
            "AddedDate": "18 Mar 2024",
            "Email": "mar@example.com",
            "Phone": "+1 65738 58937",
            "ParentImage": "assets/img/parents/parent-02.jpg",
            "StudentName": "Joann",
            "StudentImage": "assets/img/students/student-02.jpg"
        }
    ]
    return render(request, 'pages/peoples/guardian/guardian-grid.html',{'guradian_grid' : guradian_grid})

def guardian_list(request):
    guradian_list = [
        {
            "Image": "assets/img/guardians/guardian-01.jpg",
            "StudentImage" : "assets/img/students/student-01.jpg",
            "ID": "G153735",
            "GuardianName": "William",
            "Added" : "Added on 25 Mar 2024",
            "Child": "Janet",
            "Class" : "III, A",
            "Phone": "+1 82392 37359",
            "Email": "william@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-02.jpg",
            "StudentImage" : "assets/img/students/student-02.jpg",
            "ID": "G153734",
            "GuardianName": "Stacey",
            "Added" : "Added on 18 Mar 2024",
            "Child": "Joann",
            "Class" : "IV, B",
            "Phone": "+1 28249 13139",
            "Email": "stacey@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-03.jpg",
            "StudentImage" : "assets/img/students/student-03.jpg",
            "ID": "G153733",
            "GuardianName": "George",
            "Added" : "Added on 14 Mar 2024",
            "Child": "Kathleen",
            "Class" : "III, A",
            "Phone": "+1 74284 34849",
            "Email": "george@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-04.jpg",
            "StudentImage" : "assets/img/students/student-04.jpg",
            "ID": "G153732",
            "GuardianName": "Sarah",
            "Added" : "Added on 27 Feb 2024",
            "Child": "Gifford",
            "Class" : "I, B",
            "Phone": "+1 82239 42492",
            "Email": "gary@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-05.jpg",
            "StudentImage" : "assets/img/students/student-05.jpg",
            "ID": "G153731",
            "GuardianName": "Gary",
            "Added" : "Added on 11 Feb 2024",
            "Child": "Lisa",
            "Class" : "II, B",
            "Phone": "+1 82239 42492",
            "Email": "gary@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-06.jpg",
            "StudentImage" : "assets/img/students/student-06.jpg",
            "ID": "G153730",
            "GuardianName": "Linda",
            "Added" : "Added on 24 Jan 2024",
            "Child": "Ralph",
            "Class" : "III, B",
            "Phone": "+1 90139 45835",
            "Email": "linda@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-07.jpg",
            "StudentImage" : "assets/img/students/student-07.jpg",
            "ID": "G153729",
            "GuardianName": "Jeffrey",
            "Added" : "Added on 19 Jan 2024",
            "Child": "Julie",
            "Class" : "V, A",
            "Phone": "+1 23230 37402",
            "Email": "jeffrey@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-08.jpg",
            "StudentImage" : "assets/img/students/student-08.jpg",
            "ID": "G153728",
            "GuardianName": "Galina",
            "Added" : "Added on 08 Jan 2024",
            "Child": "Janet",
            "Class" : "III, A",
            "Phone": "+1 91304 34834",
            "Email": "galina@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-09.jpg",
            "StudentImage" : "assets/img/students/student-09.jpg",
            "ID": "G153727",
            "GuardianName": "Paul",
            "Added" : "Added on 22 Dec 2023",
            "Child": "Susan",
            "Class" : "VIII, B",
            "Phone": "+1 84394 28204",
            "Email": "paul@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-10.jpg",
            "StudentImage" : "assets/img/students/student-10.jpg",
            "ID": "G153726",
            "GuardianName": "Tracy",
            "Added" : "Added on 15 Dec 2024",
            "Child": "Richard",
            "Class" : "VII, B",
            "Phone": "+1 93402 39342",
            "Email": "tracy@example.com",
        },
        {
            "Image": "assets/img/guardians/guardian-11.jpg",
            "StudentImage" : "assets/img/students/student-11.jpg",
            "ID": "G153725",
            "GuardianName": "Edwin",
            "Added" : "Added on 10 Dec 2023",
            "Child": "Veronica",
            "Class" : "IX, A",
            "Phone": "+1 65738 58940",
            "Email": "edw@example.com",
        }
    ]
    return render(request, 'pages/peoples/guardian/guardian-list.html',{'guradian_list' : guradian_list})

def teacher_grid(request):
    teacher_grid = [
        {
            "ID": "T849127",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Class": "III A",
            "Email": "teresa@example.com",
            "Phone": "+1 82392 37359",
            "Subject": "Physics"
        },
        {
            "ID": "T849126",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Class": "II (A)",
            "Email": "Daniel@example.com",
            "Phone": "+1 56752 86742",
            "Subject": "Computer"
        },
        {
            "ID": "T849125",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Class": "VI (A)",
            "Email": "Hellana@example.com",
            "Phone": "+1 23566 52683",
            "Subject": "English"
        },
        {
            "ID": "T849124",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-04.jpg",
            "Name": "Erickson",
            "Class": "VI (B) , V (A)",
            "Email": "Erickson@example.com",
            "Phone": "+1 14259 85573",
            "Subject": "Spanish"
        },
        {
            "ID": "T849123",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Morgan",
            "Class": "VIII",
            "Email": "Morgan@example.com",
            "Phone": "+1 63204 35730",
            "Subject": "Env_Science"
        },
        {
            "ID": "T849122",
            "Status": "Inactive",
            "StatusClass" : "badge badge-soft-danger",
            "Image": "assets/img/teachers/teacher-06.jpg",
            "Name": "Aaron",
            "Class": "I (A)",
            "Email": "Aaron@example.com",
            "Phone": "+1 26267 80542",
            "Subject": "Chemistry"
        },
        {
            "ID": "T849121",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Class": "IV",
            "Email": "Jacquelin@example.com",
            "Phone": "+1 77502 54845",
            "Subject": "Maths"
        },
        {
            "ID": "T849120",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Raul",
            "Class": "IV",
            "Email": "Raul@example.com",
            "Phone": "+1 67845 78784",
            "Subject": "Biology"
        },
        {
            "ID": "T849119",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Class": "VII",
            "Email": "Elizabeth@example.com",
            "Phone": "+1 23566 52683",
            "Subject": "Finance"
        },
        {
            "ID": "T849118",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Class": "IX (C) , X (C)",
            "Email": "Edward@example.com",
            "Phone": "+1 14259 85573",
            "Subject": "Economics"
        },
        {
            "ID": "T849117",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Maria",
            "Class": "IX (C) , X (C)",
            "Email": "Maria@example.com",
            "Phone": "+1 97846 84518",
            "Subject": "Spanish"
        },
        {
            "ID": "T849116",
            "Status": "Active",
            "StatusClass" : "badge badge-soft-success",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacky",
            "Class": "VI (A)",
            "Email": "Jacky@example.com",
            "Phone": "+1 98392 37378",
            "Subject": "English"
        }
  ]
    return render(request, 'pages/peoples/teachers/teacher-grid.html', {'teacher_grid' : teacher_grid})

def teacher_list(request):
    teacher_list = [
        {
            "Image" : "assets/img/teachers/teacher-01.jpg",
            "ID": "T849127",
            "Name": "Teresa",
            "Class": "III A",
            "Subject": "Physics",
            "Email": "teresa@example.com",
            "Phone": "+1 82392 37359",
            "DateofJoin": "25 Mar 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-02.jpg",
            "ID": "T849126",
            "Name": "Daniel",
            "Class": "II (A)",
            "Subject": "Computer",
            "Email": "daniel@example.com",
            "Phone": "+1 56752 86742",
            "DateofJoin": "28 Mar 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-03.jpg",
            "ID": "T849125",
            "Name": "Hellana",
            "Class": "VI (A)",
            "Subject": "English",
            "Email": "hellana@example.com",
            "Phone": "+1 23566 52683",
            "DateofJoin": "11 Apr 2024",
            "Status": "Inactive",
        },
        {
            "Image" : "assets/img/teachers/teacher-06.jpg",
            "ID": "T849124",
            "Name": "Erickson",
            "Class": "I (A)",
            "Subject": "Chemistry",
            "Email": "aaron@example.com",
            "Phone": "+1 26267 80542",
            "DateofJoin": "12 May 2024",
            "Status": "Inactive",
        },
        {
            "Image" : "assets/img/teachers/teacher-07.jpg",
            "ID": "T849121",
            "Name": "Morgan",
            "Class": "IV",
            "Subject": "Maths",
            "Email": "jacquelin@example.com",
            "Phone": "+1 77502 54845",
            "DateofJoin": "20 May 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-06.jpg",
            "ID": "T849122",
            "Name": "Aaron",
            "Class": "I (A)",
            "Subject": "Chemistry",
            "Email": "aaron@example.com",
            "Phone": "+1 26267 80542",
            "DateofJoin": "12 May 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-09.jpg",
            "ID": "T849127",
            "Name": "Daniel",
            "Class": "IV",
            "Subject": "Maths",
            "Email": "jacquelin@example.com",
            "Phone": "+1 77502 54845",
            "DateofJoin": "20 May 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/students/student-10.jpg",
            "ID": "T849120",
            "Name": "Raul",
            "Class": "IX",
            "Subject": "Biology",
            "Email": "raul@example.com",
            "Phone": "+1 67845 78784",
            "DateofJoin": "27 May 2024",
            "Status": "Inactive",
        },
        {
            "Image" : "assets/img/students/student-11.jpg",
            "ID": "T849119",
            "Name": "Elizabeth",
            "Class": "VII",
            "Subject": "Economics",
            "Email": "elizabeth@example.com",
            "Phone": "+1 97846 84518",
            "DateofJoin": "10 Jun 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-03.jpg",
            "ID": "T849118",
            "Name": "Edward",
            "Class": "IX (C) , X (C)",
            "Subject": "Finance",
            "Email": "edward@example.com",
            "Phone": "+1 56187 87489",
            "DateofJoin": "18 Jun 2024",
            "Status": "Active",
        },
        {
            "Image" : "assets/img/teachers/teacher-04.jpg",
            "ID": "T849117",
            "Name": "Maria",
            "Class": "I (A)",
            "Subject": "English",
            "Email": "maria@example.com",
            "Phone": "+1 97846 84518",
            "DateofJoin": "22 Mar 2018",
            "Status": "Active",
        }
    ]
    return render(request, 'pages/peoples/teachers/teacher-list.html', {'teacher_list' : teacher_list})

    #Academic

def add_teacher(request):
    return render(request, 'pages/peoples/teachers/add-teacher.html')
    
def edit_teacher(request):
    return render(request, 'pages/peoples/teachers/edit-teacher.html')
    
def teacher_details(request):
    return render(request, 'pages/peoples/teachers/teacher-details/teacher-details.html')
 
def routine_teachers(request):
    return render(request, 'pages/peoples/teachers/teacher-details/routine-teachers.html')
 
def teacher_leaves(request):
    return render(request, 'pages/peoples/teachers/teacher-details/teacher-leaves.html')
 
def teacher_salary(request):
    return render(request, 'pages/peoples/teachers/teacher-details/teacher-salary.html')
 
def teacher_library(request):
    return render(request, 'pages/peoples/teachers/teacher-details/teacher-library.html')
 
#Academic 
 
def classes_list(request):
    classes_list = [
        {
            "ID": "C138038",
            "Class": "I",
            "Section": "A",
            "No_of_Students": "30",
            "No_of_Subjects": "3",
            "Status": "Active"
        },
        {
            "ID": "C138037",
            "Class": "I",
            "Section": "B",
            "No_of_Students": "25",
            "No_of_Subjects": "3",
            "Status": "Active",
            "Action": "Edit                                                                                                                                           Delete"
        },
        {
            "ID": "C138036",
            "Class": "II",
            "Section": "A",
            "No_of_Students": "40",
            "No_of_Subjects": "3",
            "Status": "Active"
        },
        {
            "ID": "C138035",
            "Class": "II",
            "Section": "B",
            "No_of_Students": "35",
            "No_of_Subjects": "3",
            "Status": "Active"
        },
        {
            "ID": "C138034",
            "Class": "II",
            "Section": "C",
            "No_of_Students": "25",
            "No_of_Subjects": "3",
            "Status": "Inactive"
        },
        {
            "ID": "C138033",
            "Class": "III",
            "Section": "A",
            "No_of_Students": "30",
            "No_of_Subjects": "3",
            "Status": "Active"
        },
        {
            "ID": "C138032",
            "Class": "III",
            "Section": "B",
            "No_of_Students": "25",
            "No_of_Subjects": "5",
            "Status": "Active"
        },
        {
            "ID": "C138031",
            "Class": "IV",
            "Section": "A",
            "No_of_Students": "20",
            "No_of_Subjects": "5",
            "Status": "Active"
        },
        {
            "ID": "C138030",
            "Class": "IV",
            "Section": "B",
            "No_of_Students": "30",
            "No_of_Subjects": "5",
            "Status": "Inactive"
        },
        {
            "ID": "C138029",
            "Class": "V",
            "Section": "A",
            "No_of_Students": "35",
            "No_of_Subjects": "5",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/classes/classes-list.html',{'classes_list' : classes_list})

def schedule_classes(request):
    schedule_classes = [
        {
            "ID": "S148239",
            "Type": "Class",
            "Start_Time": "09:30 AM",
            "End_Time": "10:30 AM",
            "Status": "Active"
        },
        {
            "ID": "S148238",
            "Type": "Class",
            "Start_Time": "10:30 AM",
            "End_Time": "11:30 AM",
            "Status": "Active"
        },
        {
            "ID": "S148237",
            "Type": "Class",
            "Start_Time": "11:30 AM",
            "End_Time": "12:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148236",
            "Type": "Class",
            "Start_Time": "12:30 PM",
            "End_Time": "01:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148235",
            "Type": "Class",
            "Start_Time": "01:30 PM",
            "End_Time": "02:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148234",
            "Type": "Class",
            "Start_Time": "02:30 PM",
            "End_Time": "03:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148233",
            "Type": "Class",
            "Start_Time": "03:30 PM",
            "End_Time": "04:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148232",
            "Type": "Class",
            "Start_Time": "04:30 PM",
            "End_Time": "05:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148231",
            "Type": "Class",
            "Start_Time": "05:30 PM",
            "End_Time": "06:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148230",
            "Type": "Class",
            "Start_Time": "06:30 PM",
            "End_Time": "07:30 PM",
            "Status": "Inactive"
        },
        {
            "ID": "S148239",
            "Type": "Class",
            "Start_Time": "09:30 AM",
            "End_Time": "10:30 AM",
            "Status": "Active"
        },
        {
            "ID": "S148238",
            "Type": "Class",
            "Start_Time": "10:30 AM",
            "End_Time": "11:30 AM",
            "Status": "Active"
        },
        {
            "ID": "S148237",
            "Type": "Class",
            "Start_Time": "11:30 AM",
            "End_Time": "12:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148236",
            "Type": "Class",
            "Start_Time": "12:30 PM",
            "End_Time": "01:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148235",
            "Type": "Class",
            "Start_Time": "01:30 PM",
            "End_Time": "02:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148234",
            "Type": "Class",
            "Start_Time": "02:30 PM",
            "End_Time": "03:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148233",
            "Type": "Class",
            "Start_Time": "03:30 PM",
            "End_Time": "04:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148232",
            "Type": "Class",
            "Start_Time": "04:30 PM",
            "End_Time": "05:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148231",
            "Type": "Class",
            "Start_Time": "05:30 PM",
            "End_Time": "06:30 PM",
            "Status": "Active"
        },
        {
            "ID": "S148230",
            "Type": "Class",
            "Start_Time": "06:30 PM",
            "End_Time": "07:30 PM",
            "Status": "Inactive"
        }
    ]
    return render(request, 'pages/academic/classes/schedule-classes.html', {'schedule_classes' : schedule_classes })

def class_room(request):
    class_room = [
        {
            "ID": "R167648",
            "Room_No": "101",
            "Capacity": "50",
            "Status": "Active"
        },
        {
            "ID": "R167647",
            "Room_No": "102",
            "Capacity": "40",
            "Status": "Active"
        },
        {
            "ID": "R167646",
            "Room_No": "103",
            "Capacity": "60",
            "Status": "Active"
        },
        {
            "ID": "R167645",
            "Room_No": "104",
            "Capacity": "50",
            "Status": "Active"
        },
        {
            "ID": "R167644",
            "Room_No": "105",
            "Capacity": "40",
            "Status": "Active"
        },
        {
            "ID": "R167643",
            "Room_No": "106",
            "Capacity": "50",
            "Status": "Active"
        },
        {
            "ID": "R167642",
            "Room_No": "107",
            "Capacity": "40",
            "Status": "Active"
        },
        {
            "ID": "R167641",
            "Room_No": "108",
            "Capacity": "40",
            "Status": "Active"
        },
        {
            "ID": "R167640",
            "Room_No": "109",
            "Capacity": "40",
            "Status": "Active"
        },
        {
            "ID": "R167639",
            "Room_No": "110",
            "Capacity": "50",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/class-room.html', {'class_room' : class_room})

def class_routine(request):
    class_routine = [
        {
            "ID": "RT167648",
            "Class": "I",
            "Section": "A",
            "Teacher": "Erickson",
            "Subject": "English",
            "Day": "Monday",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Class_Room": "101"
        },
        {
            "ID": "RT167647",
            "Class": "I",
            "Section": "B",
            "Teacher": "Mori",
            "Subject": "Math",
            "Day": "Tuesday",
            "Start_Time": "10:45 AM",
            "End_Time": "12:00 PM",
            "Class_Room": "102"
        },
        {
            "ID": "RT167646",
            "Class": "II",
            "Section": "A",
            "Teacher": "Joseph",
            "Subject": "Physics",
            "Day": "Wednesday",
            "Start_Time": "12:00 PM",
            "End_Time": "01:15 PM",
            "Class_Room": "103"
        },
        {
            "ID": "RT167645",
            "Class": "II",
            "Section": "B",
            "Teacher": "James",
            "Subject": "Chemsitry",
            "Day": "Thursday",
            "Start_Time": "01:15 PM",
            "End_Time": "02:30 PM",
            "Class_Room": "104"
        },
        {
            "ID": "RT167644",
            "Class": "II",
            "Section": "C",
            "Teacher": "Biology",
            "Subject": "Biology",
            "Day": "Friday",
            "Start_Time": "02:30 PM",
            "End_Time": "03:45 PM",
            "Class_Room": "105"
        },
        {
            "ID": "RT167643",
            "Class": "III",
            "Section": "A",
            "Teacher": "Teresa",
            "Subject": "Higher Math",
            "Day": "Saturday",
            "Start_Time": "03:45 PM",
            "End_Time": "05:00 PM",
            "Class_Room": "106"
        },
        {
            "ID": "RT167642",
            "Class": "III",
            "Section": "B",
            "Teacher": "James",
            "Subject": "Information Technology",
            "Day": "Monday",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Class_Room": "107"
        },
        {
            "ID": "RT167641",
            "Class": "IV",
            "Section": "A",
            "Teacher": "Hendrita",
            "Subject": "Moral Education",
            "Day": "Tuesday",
            "Start_Time": "10:45 AM",
            "End_Time": "12:00 PM",
            "Class_Room": "108"
        },
        {
            "ID": "RT167640",
            "Class": "IV",
            "Section": "B",
            "Teacher": "Morgan",
            "Subject": "Finance",
            "Day": "Wednesday",
            "Start_Time": "12:00 PM",
            "End_Time": "01:15 PM",
            "Class_Room": "109"
        },
        {
            "ID": "RT167639",
            "Class": "V",
            "Section": "A",
            "Teacher": "Ramsey",
            "Subject": "Economics",
            "Day": "Thursday",
            "Start_Time": "01:15 PM",
            "End_Time": "02:30 PM",
            "Class_Room": "110"
        }
    ]
    return render(request, 'pages/academic/class-routine.html', {'class_routine' : class_routine})

def class_section(request):
    class_section = [
        {
            "ID": "SE167645",
            "Section_Name": "A",
            "Status": "Active"
        },
        {
            "ID": "SE167644",
            "Section_Name": "B",
            "Status": "Active"
        },
        {
            "ID": "SE167643",
            "Section_Name": "C",
            "Status": "Active"
        },
        {
            "ID": "SE167642",
            "Section_Name": "D",
            "Status": "Active"
        },
        {
            "ID": "SE167641",
            "Section_Name": "E",
            "Status": "Active"
        },
        {
            "ID": "SE167640",
            "Section_Name": "F",
            "Status": "Active"
        },
        {
            "ID": "SE167639",
            "Section_Name": "G",
            "Status": "Active"
        },
        {
            "ID": "SE167638",
            "Section_Name": "H",
            "Status": "Active"
        },
        {
            "ID": "SE167637",
            "Section_Name": "I",
            "Status": "Active"
        },
        {
            "ID": "SE167636",
            "Section_Name": "J",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/class-section.html', {'class_section' : class_section})

def class_subject(request):
    class_subject = [
        {
            "ID": "SU128394",
            "Name": "English",
            "Code": "101",
            "Type": "Theory",
            "Status": "Active"
        },
        {
            "ID": "SU128393",
            "Name": "Math",
            "Code": "102",
            "Type": "Theory",
            "Status": "Active"
        },
        {
            "ID": "SU128392",
            "Name": "Physics",
            "Code": "103",
            "Type": "Practical",
            "Status": "Active"
        },
        {
            "ID": "SU128391",
            "Name": "Chemistry",
            "Code": "104",
            "Type": "Practical",
            "Status": "Active"
        },
        {
            "ID": "SU128390",
            "Name": "Biology",
            "Code": "105",
            "Type": "Practical",
            "Status": "Inactive"
        },
        {
            "ID": "SU128389",
            "Name": "Higher Math",
            "Code": "106",
            "Type": "Practical",
            "Status": "Active"
        },
        {
            "ID": "SU128388",
            "Name": "Information Technology",
            "Code": "107",
            "Type": "Practical",
            "Status": "Active"
        },
        {
            "ID": "SU128387",
            "Name": "Moral Education",
            "Code": "108",
            "Type": "Practical",
            "Status": "Inactive"
        },
        {
            "ID": "SU128388",
            "Name": "Finance",
            "Code": "109",
            "Type": "Thory",
            "Status": "Active"
        },
        {
            "ID": "SU128386",
            "Name": "Economics",
            "Code": "110",
            "Type": "Theory",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/class-subject.html', {"class_subject" : class_subject})

def class_syllabus(request):
    class_syllabus = [
        {
            "Class": "I",
            "Section": "A",
            "Subject_Group": "I, C English",
            "Created_Date": "10 May 2024",
            "Status": "Active"
        },
        {
            "Class": "I",
            "Section": "B",
            "Subject_Group": "III, A Maths",
            "Created_Date": "11 May 2024",
            "Status": "Active"
        },
        {
            "Class": "II",
            "Section": "A",
            "Subject_Group": "II, A English",
            "Created_Date": "12 May 2024",
            "Status": "Active"
        },
        {
            "Class": "II",
            "Section": "B",
            "Subject_Group": "IV, A Physics",
            "Created_Date": "13 May 2024",
            "Status": "Active"
        },
        {
            "Class": "II",
            "Section": "C",
            "Subject_Group": "V, A Chemistry",
            "Created_Date": "14 May 2024",
            "Status": "Active"
        },
        {
            "Class": "III",
            "Section": "A",
            "Subject_Group": "III, B Maths",
            "Created_Date": "15 May 2024",
            "Status": "Active"
        },
        {
            "Class": "III",
            "Section": "B",
            "Subject_Group": "IV, B Chemistry",
            "Created_Date": "16 May 2024",
            "Status": "Active"
        },
        {
            "Class": "IV",
            "Section": "A",
            "Subject_Group": "I, B Maths",
            "Created_Date": "17 May 2024",
            "Status": "Active"
        },
        {
            "Class": "IV",
            "Section": "B",
            "Subject_Group": "VI, B Chemistry",
            "Created_Date": "18 May 2024",
            "Status": "Active"
        },
        {
            "Class": "V",
            "Section": "A",
            "Subject_Group": "IV, D Maths",
            "Created_Date": "19 May 2024",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/class-syllabus.html', {"class_syllabus" : class_syllabus})

def class_time_table(request):
    return render(request, 'pages/academic/class-time-table.html', {'class_time_table' : class_time_table})

def class_home_work(request):
    class_home_work = [
        {
            "ID": "HW1783929",
            "Class": "I",
            "Section": "A",
            "Subject": "English",
            "Homework_Date": "10 May 2024",
            "Submission_Date": "12 May 2024",
            "Image": "assets/img/students/student-01.jpg",
            "Created_By": "Janet"
        },
        {
            "ID": "HW1783928",
            "Class": "I",
            "Section": "B",
            "Subject": "Math",
            "Homework_Date": "11 May 2024",
            "Submission_Date": "13 May 2024",
            "Image": "assets/img/students/student-02.jpg",
            "Created_By": "Joann"
        },
        {
            "ID": "HW1783927",
            "Class": "II",
            "Section": "A",
            "Subject": "Physics",
            "Homework_Date": "12 May 2024",
            "Submission_Date": "14 May 2024",
            "Image": "assets/img/students/student-03.jpg",
            "Created_By": "Kathleen"
        },
        {
            "ID": "HW1783926",
            "Class": "II",
            "Section": "B",
            "Subject": "Chemsitry",
            "Homework_Date": "13 May 2024",
            "Submission_Date": "15 May 2024",
            "Image": "assets/img/students/student-04.jpg",
            "Created_By": "Gifford"
        },
        {
            "ID": "HW1783925",
            "Class": "II",
            "Section": "C",
            "Subject": "Biology",
            "Homework_Date": "14 May 2024",
            "Submission_Date": "16 May 2024",
            "Image": "assets/img/students/student-05.jpg",
            "Created_By": "Lisa"
        },
        {
            "ID": "HW1783924",
            "Class": "III",
            "Section": "A",
            "Subject": "Higher Math",
            "Homework_Date": "15 May 2024",
            "Submission_Date": "17 May 2024",
            "Image": "assets/img/students/student-06.jpg",
            "Created_By": "Ralph"
        },
        {
            "ID": "HW1783923",
            "Class": "III",
            "Section": "B",
            "Subject": "Information Technology",
            "Homework_Date": "16 May 2024",
            "Submission_Date": "18 May 2024",
            "Image": "assets/img/students/student-07.jpg",
            "Created_By": "Julie"
        },
        {
            "ID": "HW1783922",
            "Class": "IV",
            "Section": "A",
            "Subject": "Moral Education",
            "Homework_Date": "17 May 2024",
            "Submission_Date": "19 May 2024",
            "Image": "assets/img/students/student-08.jpg",
            "Created_By": "Ryan"
        },
        {
            "ID": "HW1783921",
            "Class": "IV",
            "Section": "B",
            "Subject": "Finance",
            "Homework_Date": "18 May 2024",
            "Submission_Date": "20 May 2024",
            "Image": "assets/img/students/student-09.jpg",
            "Created_By": "Susan"
        },
        {
            "ID": "HW1783920",
            "Class": "V",
            "Section": "A",
            "Subject": "Economics",
            "Homework_Date": "19 May 2024",
            "Submission_Date": "21 May 2024",
            "Image": "assets/img/students/student-12.jpg",
            "Created_By": "Richard"
        }
    ]
    return render(request, 'pages/academic/class-home-work.html', {"class_home_work" : class_home_work})
                         
def academic_reasons(request):
    academic_reasons = [
        {
            "Role": "Teacher",
            "Reason": "Pregnancy",
            "Created_Date": "24 May 2024"
        },
        {
            "Role": "Student",
            "Reason": "Fees Unpaid",
            "Created_Date": "21 May 2024"
        },
        {
            "Role": "Staff",
            "Reason": "Complaint",
            "Created_Date": "16 May 2024"
        },
        {
            "Role": "Student",
            "Reason": "Complaint",
            "Created_Date": "15 May 2024"
        },
        {
            "Role": "Staff",
            "Reason": "Complaint",
            "Created_Date": "28 Apr 2024"
        },
        {
            "Role": "Student",
            "Reason": "Fail in all Subject",
            "Created_Date": "26 Apr 2024"
        },
        {
            "Role": "Staff",
            "Reason": "Engage",
            "Created_Date": "22 May 2024"
        },
        {
            "Role": "Student",
            "Reason": "Experience",
            "Created_Date": "16 Apr 2024"
        },
        {
            "Role": "Staff",
            "Reason": "No Improvement",
            "Created_Date": "14 Apr 2024"
        },
        {
            "Role": "Staff",
            "Reason": "Issue in family",
            "Created_Date": "12 May 2024"
        }
    ]
    return render(request, 'pages/academic/academic-reasons.html', {"academic_reasons" : academic_reasons})

def exam_list(request):
    exam_list = [
        {
            "ID": "E140523",
            "Exam_Name": "Week Test",
            "Exam_Date": "13 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM"
        },
        {
            "ID": "E140522",
            "Exam_Name": "Mothly Test",
            "Exam_Date": "27 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "11:00 AM"
        },
        {
            "ID": "E140521",
            "Exam_Name": "Chapter Wise Test",
            "Exam_Date": "05 Jun 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:30 AM"
        },
        {
            "ID": "E140520",
            "Exam_Name": "Unit Test",
            "Exam_Date": "15 Jun 2024",
            "Start_Time": "10:30 AM",
            "End_Time": "11:30 AM"
        },
        {
            "ID": "E140519",
            "Exam_Name": "Progress Test",
            "Exam_Date": "20 Jun 2024",
            "Start_Time": "11:00 AM",
            "End_Time": "12:00 PM"
        },
        {
            "ID": "E140518",
            "Exam_Name": "Oral Test",
            "Exam_Date": "03 Jul 2024",
            "Start_Time": "12:30 PM",
            "End_Time": "01:30 PM"
        },
        {
            "ID": "E140517",
            "Exam_Name": "Semester Exam",
            "Exam_Date": "18 Jul 2024",
            "Start_Time": "10:30 AM",
            "End_Time": "12:30 PM"
        },
        {
            "ID": "E140516",
            "Exam_Name": "Quaterly Exam",
            "Exam_Date": "26 Aug 2024",
            "Start_Time": "09:00 AM",
            "End_Time": "12:00 PM"
        },
        {
            "ID": "E140515",
            "Exam_Name": "Half Yearly Exam",
            "Exam_Date": "15 Nov 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "12:30 PM"
        },
        {
            "ID": "E140514",
            "Exam_Name": "Annual Exam",
            "Exam_Date": "10 Mar 2025",
            "Start_Time": "10:00 AM",
            "End_Time": "01:00 PM"
        }
    ]
    return render(request, 'pages/academic/examinations/exam-list.html', {"exam_list" : exam_list})

def exam_schedule(request):
    exam_schedule = [
        {
            "Subject": "English",
            "Exam_Date": "13 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "101",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Spanish",
            "Exam_Date": "14 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "104",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Physics",
            "Exam_Date": "15 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "103",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Chemistry",
            "Exam_Date": "16 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "105",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Maths",
            "Exam_Date": "17 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "106",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Computer",
            "Exam_Date": "18 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "102",
            "Max_Marks": "100",
            "Min_Marks": "35"
        },
        {
            "Subject": "Env_Science",
            "Exam_Date": "19 May 2024",
            "Start_Time": "09:30 AM",
            "End_Time": "10:45 AM",
            "Duration": "3 hrs",
            "Room_No": "107",
            "Max_Marks": "100",
            "Min_Marks": "35"
        }
    ]
    return render(request, 'pages/academic/examinations/exam-schedule.html', {"exam_schedule" : exam_schedule})

def grade(request):
    grade = [
        {
            "ID": "G180482",
            "Grade": "O",
            "Percentage": "90% - 100%",
            "Grade_Points": "10",
            "Status": "Active"
        },
        {
            "ID": "G180481",
            "Grade": "A+",
            "Percentage": "80% - 90%",
            "Grade_Points": "8",
            "Status": "Active"
        },
        {
            "ID": "G180480",
            "Grade": "A",
            "Percentage": "70% - 80%",
            "Grade_Points": "6",
            "Status": "Active"
        },
        {
            "ID": "G180479",
            "Grade": "B+",
            "Percentage": "60% - 70%",
            "Grade_Points": "4",
            "Status": "Active"
        },
        {
            "ID": "G180478",
            "Grade": "B",
            "Percentage": "50% - 60%",
            "Grade_Points": "3",
            "Status": "Active"
        },
        {
            "ID": "G180477",
            "Grade": "C+",
            "Percentage": "40% - 50%",
            "Grade_Points": "2",
            "Status": "Active"
        },
        {
            "ID": "G180476",
            "Grade": "C",
            "Percentage": "35% - 40%",
            "Grade_Points": "1",
            "Status": "Active"
        },
        {
            "ID": "G180475",
            "Grade": "F",
            "Percentage": "Below 35%",
            "Grade_Points": "0",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/academic/examinations/grade.html', {"grade" : grade})

def exam_attendance(request):
    exam_attendance = [
        {
            "ID": "EA123794",
            "Image": "assets/img/students/student-01.jpg",
            "Student_Name": "Janet",
            "Roll_No" : "35013",            
            "English": 'present',
            "Spanish": 'present',
            "Physics" : 'present', 
            "Chemistry" : 'present', 
            "Maths" : 'present', 
            "Computer" : 'present', 
            "Env_Science" : 'present'           
        },        
        {
            "ID": "EA123793",
            "Image": "assets/img/students/student-02.jpg",
            "Student_Name": "Joann",
            "Roll_No" : "35012",
            "English": "present",
            "Spanish": "absent",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123792",
            "Image": "assets/img/students/student-03.jpg",
            "Student_Name": "Kathleen",
            "Roll_No" : "35011",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "absent",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123791",
            "Image": "assets/img/students/student-04.jpg",
            "Student Name": "Gifford",
            "Roll_No" : "35010",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123790",
            "Image": "assets/img/students/student-05.jpg",
            "Student Name": "Lisa", 
            "Roll_No" : "35009",
            "English": "present",
            "Spanish": "present",
            "Physics": " ",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123789",
            "Image": "assets/img/students/student-06.jpg",
            "Student Name": "Ralph", 
            "Roll No" : "35008",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123788",
            "Image": "assets/img/students/student-07.jpg",
            "Student Name": "Julie",
            "Roll_No" : "35007",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": " ",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123787",
            "Image": "assets/img/students/student-08.jpg",
            "Student Name": "Ryan",
            "Roll_No" : "35006",
            "English": "present",
            "Spanish": "absent",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        },
        {
            "ID": "EA123786",
            "Image": "assets/img/students/student-09.jpg",
            "Student Name": "Susan", 
            "Roll_No" : "35004",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "absent",
            "Env_Science": "present"
        }, 
        {
            "ID": "EA123785",
            "Image": "assets/img/students/student-10.jpg",
            "Student Name": "Richard", 
            "Roll_No" : "35003",
            "English": "present",
            "Spanish": "present",
            "Physics": "present",
            "Chemistry": "present",
            "Maths": "present",
            "Computer": "present",
            "Env_Science": "present"
        }
    ]
    return render(request, 'pages/academic/examinations/exam-attendance.html', {"exam_attendance": exam_attendance})

def exam_results(request):
    exam_results = [
        {
            "Admission_No": "AD9892434",
            "Image": "assets/img/students/student-01.jpg",
            "Student_Name": "Janet",
            "Roll_No" : "35013",
            "English": '95',
            "Spanish": "93",
            "Physics": "88",
            "Chemistry": "90",
            "Maths": "85",
            "Computer": "98",
            "Env_Science": '95',
            "Total": "644",
            "Percent": "92",
            "Grade": "O",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892433",
            "Image": "assets/img/students/student-02.jpg",
            "Student_Name": "Joann",
            "Roll_No" : "35012",
            "English": "30",
            "Spanish": "35",
            "Physics": "36",
            "Chemistry": "28",
            "Maths": "38",
            "Computer": "40",
            "Env_Science": "37",
            "Total": "244",
            "Percent": "34",
            "Grade": "F",
            "Result": "Fail"
        },
        {
            "Admission_No": "AD9892432",
            "Image": "assets/img/students/student-03.jpg",
            "Student_Name": "Kathleen", 
            "Roll_No" : "35011",
            "English": "70",
            "Spanish": "80",
            "Physics": "85",
            "Chemistry": "78",
            "Maths": "82",
            "Computer": "83",
            "Env_Science": "80",
            "Total": "558",
            "Percent": "79",
            "Grade": "A",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892431",
            "Image": "assets/img/students/student-04.jpg",
            "Student_Name": "Gifford", 
            "Roll_No" : "35010",
            "English": "60",
            "Spanish": "68",
            "Physics": "65",
            "Chemistry": "70",
            "Maths": "67",
            "Computer": "72",
            "Env_Science": "75",
            "Total": "477",
            "Percent": "68",
            "Grade": "B+",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892430",
            "Image": "assets/img/students/student-05.jpg",
            "Student_Name": "Lisa", 
            "Roll_No" : "35009",
            "English": "36",
            "Spanish": "30",
            "Physics": "40",
            "Chemistry": "38",
            "Maths": "50",
            "Computer": "48",
            "Env_Science": "43",
            "Total": "285",
            "Percent": "40",
            "Grade": "F",
            "Result": "Fail"
        },
        {
            "Admission_No": "AD9892429",
            "Image": "assets/img/students/student-06.jpg",
            "Student_Name": "Ralph", 
            "Roll_No" : "35008",
            "English": "43",
            "Spanish": "50",
            "Physics": "62",
            "Chemistry": "70",
            "Maths": "65",
            "Computer": "58",
            "Env_Science": "60",
            "Total": "408",
            "Percent": "58",
            "Grade": "B",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892428",
            "Image": "assets/img/students/student-07.jpg",
            "Student_Name": "Julie", 
            "Roll_No" : "35007",
            "English": "72",
            "Spanish": "80",
            "Physics": "75",
            "Chemistry": "78",
            "Maths": "84",
            "Computer": "87",
            "Env_Science": "76",
            "Total": "552",
            "Percent": "78",
            "Grade": "A",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892427",
            "Image": "assets/img/students/student-08.jpg",
            "Student_Name": "Ryan",
            "Roll_No" : "35006",
            "English": "40",
            "Spanish": "48",
            "Physics": "42",
            "Chemistry": "47",
            "Maths": "32",
            "Computer": "58",
            "Env_Science": "50",
            "Total": "317",
            "Percent": "45",
            "Grade": "F",
            "Result": "Fail"
        },
        {
            "Admission_No": "AD9892426",
            "Image": "assets/img/students/student-09.jpg",
            "Student_Name": "Susan",
            "Roll_No" : "35004",
            "English": "60",
            "Spanish": "62",
            "Physics": "65",
            "Chemistry": "70",
            "Maths": "72",
            "Computer": "63",
            "Env_Science": "78",
            "Total": "470",
            "Percent": "67",
            "Grade": "B+",
            "Result": "Pass"
        },
        {
            "Admission_No": "AD9892425",
            "Image": "assets/img/students/student-10.jpg",
            "Student_Name": "Susan",
            "Roll_No" : "35004",
            "English": "72",
            "Spanish": "78",
            "Physics": "85",
            "Chemistry": "83",
            "Maths": "86",
            "Computer": "90",
            "Env_Science": "92",
            "Total": "586",
            "Percent": "83",
            "Grade": "A+",
            "Result": "Pass"
        }
    ]
    return render(request, 'pages/academic/examinations/exam-results.html', {"exam_results" : exam_results })

    # HRM    

#Hrm 

def staffs_list(request):
    staffs_list = [
        {
            "ID": "8198",
            "Image": "assets/img/profiles/avatar-27.jpg",
            "Name": "Kevin",
            "Department": "Admin",
            "Designation": "Technical Head",
            "Phone": "+1 63423 72397",
            "Email": "kevin@example.com",
            "Date_of_Join": "10 Mar 2024"
        },
        {
            "ID": "8197",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Willie",
            "Department": "Management",
            "Designation": "Receptionist",
            "Phone": "+1 82913 61371",
            "Email": "willie@example.com",
            "Date_of_Join": "16 Mar 2024"
        },
        {
            "ID": "8196",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Department": "Management",
            "Designation": "Admin",
            "Phone": "+1 56752 86742",
            "Email": "daniel@example.com",
            "Date_of_Join": "28 Mar 2024"
        },
        {
            "ID": "8195",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Department": "Management",
            "Designation": "Admin",
            "Phone": "+1 82392 37359",
            "Email": "teresa@example.com",
            "Date_of_Join": "25 Mar 2024"
        },
        {
            "ID": "8194",
            "Image": "assets/img/teachers/teacher-06.jpg",
            "Name": "Johnson",
            "Department": "Finance",
            "Designation": "Accountant",
            "Phone": "+1 53619 54691",
            "Email": "johnson@example.com",
            "Date_of_Join": "04 Apr 2024"
        },
        {
            "ID": "8193",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Department": "Management",
            "Designation": "HR Manager",
            "Phone": "+1 23566 52683",
            "Email": "hellana@example.com",
            "Date_of_Join": "11 Apr 2024"
        },
        {
            "ID": "8192",
            "Image": "assets/img/members/members-01.jpg",
            "Name": "James",
            "Department": "Library",
            "Designation": "Librarian",
            "Phone": "+1 78429 82414",
            "Email": "james@example.com",
            "Date_of_Join": "22 Apr 2024"
        },
        {
            "ID": "8191",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Department": "Transport",
            "Designation": "Driver",
            "Phone": "+1 77502 54845",
            "Email": "jacquelin@example.com",
            "Date_of_Join": "20 May 2024"
        },
        {
            "ID": "8190",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Department": "Finance",
            "Designation": "Accounts Manager",
            "Phone": "+1 56187 87489",
            "Email": "edward@example.com",
            "Date_of_Join": "10 Jun 2024"
        },
        {
            "FIELD1": "",
            "ID": "8189",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Department": "Management",
            "Designation": "Receptionist",
            "Phone": "+1 97846 84518",
            "Email": "elizabeth@example.com",
            "Date_of_Join": "18 Jun 2024"
        }
    ]
    return render(request, 'pages/hrm/staffs-list.html', {"staffs_list" : staffs_list})                         

def add_staff(request):
    return render(request, 'pages/hrm/add-staff.html')
    
def edit_staff(request):
    return render(request, 'pages/hrm/edit-staff.html')

def departments(request):
    departments = [
        {
            "ID": "D757248",
            "Department": "Admin",
            "Status": "Active"
        },
        {
            "ID": "D757247",
            "Department": "Finance",
            "Status": "Active"
        },
        {
            "ID": "D757246",
            "Department": "Academic",
            "Status": "Active"
        },
        {
            "ID": "D757245",
            "Department": "Library",
            "Status": "Active"
        },
        {
            "ID": "D757244",
            "Department": "Health",
            "Status": "Inactive"
        },
        {
            "ID": "D757243",
            "Department": "Transport",
            "Status": "Active"
        },
        {
            "ID": "D757242",
            "Department": "Hostel",
            "Status": "Active"
        },
        {
            "ID": "D757241",
            "Department": "Management",
            "Status": "Active"
        },
        {
            "ID": "D757240",
            "Department": "Guidance",
            "Status": "Inactive"
        },
        {
            "ID": "D757239",
            "Department": "Sports",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/hrm/departments.html', {"departments" : departments})

def designation(request): 
    designation = [
        {
            "ID": "DS748294",
            "Designation": "Technical Head",
            "Status": "Active"
        },
        {
            "ID": "DS748293",
            "Designation": "Accountant",
            "Status": "Active"
        },
        {
            "ID": "DS748292",
            "Designation": "Teacher",
            "Status": "Active"
        },
        {
            "ID": "DS748291",
            "Designation": "Librarian",
            "Status": "Active"
        },
        {
            "ID": "DS748290",
            "Designation": "Doctor",
            "Status": "Inactive"
        },
        {
            "ID": "DS748289",
            "Designation": "Driver",
            "Status": "Active"
        },
        {
            "ID": "DS748288",
            "Designation": "Warden",
            "Status": "Active"
        },
        {
            "ID": "DS748287",
            "Designation": "Receptionist",
            "Status": "Active"
        },
        {
            "ID": "DS748286",
            "Designation": "Therapist",
            "Status": "Inactive"
        },
        {
            "ID": "DS748285",
            "Designation": "Coach",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/hrm/designation.html', {"designation" : designation})

def student_attendance(request):
    student_attendance = [
        {
            "Admission_No": "AD9892434",
            "Image": "assets/img/students/student-01.jpg",
            "Roll_No": "35013",
            "Name": "Janet",
            "Class": "III",
            "Section": "A",
            "Attendance": "Present"
        },
        {
            "Admission_No": "AD9892433",
            "Image": "assets/img/students/student-02.jpg",
            "Roll_No": "35012",
            "Name": "Joann",
            "Class": "IV",
            "Section": "B",
            "Attendance": "Present"
        },
        {
            "Admission_No": "AD9892432",
            "Image": "assets/img/students/student-03.jpg",
            "Roll_No": "35011",
            "Name": "Kathleen",
            "Class": "II",
            "Section": "A",
            "Attendance": "Present"
        },
        {
            "Admission_No": "AD9892431",
            "Image": "assets/img/students/student-04.jpg",
            "Roll_No": "35010",
            "Name": "Gifford",
            "Class": "I",
            "Section": "B",
            "Attendance": "Late"
        },
        {
            "Admission_No": "AD9892430",
            "Image": "assets/img/students/student-05.jpg",
            "Roll_No": "35009",
            "Name": "Lisa",
            "Class": "II",
            "Section": "B",
            "Attendance": "Holiday"
        },
        {
            "Admission_No": "AD9892429",
            "Image": "assets/img/students/student-06.jpg",
            "Roll_No": "35008",
            "Name": "Ralph",
            "Class": "II",
            "Section": "B",
            "Attendance": "Halfday"
        },
        {
            "Admission_No": "AD9892428",
            "Image": "assets/img/students/student-07.jpg",
            "Roll_No": "35007",
            "Name": "Julie",
            "Class": "V",
            "Section": "A",
            "Attendance": "Late"
        },
        {
            "Admission_No": "AD9892427",
            "Image": "assets/img/students/student-08.jpg",
            "Roll_No": "35006",
            "Name": "Ryan",
            "Class": "VI",
            "Section": "A",
            "Attendance": "Present"
        },
        {
            "Admission_No": "AD9892426",
            "Image": "assets/img/students/student-09.jpg",
            "Roll_No": "35005",
            "Name": "Susan",
            "Class": "VIII",
            "Section": "B",
            "Attendance": "Absent"
        },
        {
            "Admission_No": "AD9892425",
            "Image": "assets/img/students/student-10.jpg",
            "Roll_No": "35004",
            "Name": "Richard",
            "Class": "VII",
            "Section": "B",
            "Attendance": "Absent"
        }
    ]
    return render(request, 'pages/hrm/attendance/student-attendance.html', {"student_attendance" : student_attendance})

def teacher_attendance(request):
    teacher_attendance = [
        {
            "ID": "T849127",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Janet",
            "Class": "III A",
            "Attendance": "Present"
        },
        {
            "ID": "T849126",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Class": "II (A)",
            "Attendance": "Present"
        },
        {
            "ID": "T849125",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Hellana",
            "Class": "VI (A)",
            "Attendance": "Present"
        },
        {
            "ID": "T849124",
            "Image": "assets/img/teachers/teacher-04.jpg",
            "Name": "Erickson",
            "Class": "VI (B) , V (A)",
            "Attendance": "Present",
        },
        {
            "ID": "T849123",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Morgan",
            "Class": "VIII",
            "Attendance": "Present"
        },
        {
            "ID": "T849122",
            "Image": "assets/img/teachers/teacher-06.jpg",
            "Name": "Aaron",
            "Class": "I (A)",
            "Attendance": "Present"
        },
        {
            "ID": "T849121",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Class": "IV",
            "Attendance": "Present"
        },
        {
            "ID": "T849120",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Raul",
            "Class": "IX",
            "Attendance": "Present"
        },
        {
            "ID": "T849119",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Class": "VII",
            "Attendance": "Present"
        },
        {
            "ID": "T849118",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Class": "IX (C) , X (C)",
            "Attendance": "Present"
        }
    ]
    return render(request, 'pages/hrm/attendance/teacher-attendance.html', {"teacher_attendance" : teacher_attendance})

def staff_attendance(request):
    staff_attendance = [
        {
            "ID": "ST738198",
            "Image": "assets/img/profiles/avatar-27.jpg",
            "Name": "Kevin",
            "Department": "Admin",
            "Designation": "Technical Head",
            "Attendance": "Present"
        },
        {
            "ID": "ST738197",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Willie",
            "Department": "Management",
            "Designation": "Receptionist",
            "Attendance": "Present"
        },
        {
            "ID": "ST738196",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Department": "Management",
            "Designation": "Admin",
            "Attendance": "Present"
        },
        {
            "ID": "ST738195",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Department": "Management",
            "Designation": "Admin",
            "Attendance": "Present"
        },
        {
            "ID": "ST738194",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Johnson",
            "Department": "Finance",
            "Designation": "Accountant",
            "Attendance": "Present"
        },
        {
            "ID": "ST738193",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Department": "Management",
            "Designation": "HR Manager",
            "Attendance": "Present"
        },
        {
            "ID": "ST738192",
            "Image": "assets/img/members/members-01.jpg",
            "Name": "James",
            "Department": "Library",
            "Designation": "Librarian",
            "Attendance": "Present"
        },
        {
            "ID": "ST738191",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Department": "Transport",
            "Designation": "Driver",
            "Attendance": "Present"
        },
        {
            "ID": "ST738190",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Department": "Finance",
            "Designation": "Accounts Manager",
            "Attendance": "Present"
        },
        {
            "ID": "ST738189",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Department": "Management",
            "Designation": "Receptionist",
            "Attendance": "Present"
        }
    ]
    return render(request, 'pages/hrm/attendance/staff-attendance.html', {"staff_attendance" : staff_attendance})

def list_leaves(request):
    list_leaves = [
        {
            "ID": "LT748294",
            "Leave_Type": "Medical Leave",
            "Status": "Active"
        },
        {
            "ID": "LT748293",
            "Leave_Type": "Casual Leave",
            "Status": "Active"
        },
        {
            "ID": "LT748292",
            "Leave_Type": "Maternity Leave",
            "Status": "Active"
        },
        {
            "ID": "LT748291",
            "Leave_Type": "Sick Leave",
            "Status": "Active"
        },
        {
            "ID": "LT748290",
            "Leave_Type": "Paternity Leave",
            "Status": "Inactive"
        },
        {
            "ID": "LT748289",
            "Leave_Type": "Special Leave",
            "Status": "Inactive"
        }
    ]
    return render(request, 'pages/hrm/leaves/list-leaves.html', {"list_leaves" : list_leaves })

def approve_request(request):
    approve_request = [
        {
            "Submitted_By": "James Deckar (9004)",
            "Leave_Type": "Medical Leave",
            "Role": "Student",
            "Leave_Date": "05 May 2024 - 07 may 2024",
            "No_of_Days": "5",
            "Applied_On": "05 May 2024",
            "Authority": "Jacquelin",
            "Status": "Approved"
        },
        {
            "Submitted_By": "Richard (2145)",
            "Leave_Type": "Casual Leave",
            "Role": "Teacher",
            "Leave_Date": "07 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "07 May 2024",
            "Authority": "Elizabeth",
            "Status": "Approved"
        },
        {
            "Submitted_By": "Susan (4147)",
            "Leave_Type": "Maternity Leave",
            "Role": "Admin",
            "Leave_Date": "08 May 2024 - 19 may 2024",
            "No_of_Days": "10",
            "Applied_On": "02 May 2024",
            "Authority": "Teresa",
            "Status": "Approved"
        },
        {
            "Submitted_By": "Lisa (2145)",
            "Leave_Type": "Sick Leave",
            "Role": "Librarian",
            "Leave_Date": "05 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "04 May 2024",
            "Authority": "Edward",
            "Status": "Approved"
        },
        {
            "Submitted_By": "Janet (1457)",
            "Leave_Type": "Paternity Leave",
            "Role": "Driver",
            "Leave_Date": "07 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "06 May 2024",
            "Authority": "Daniel",
            "Status": "Disapproved"
        },
        {
            "Submitted_By": "Ryan (9784)",
            "Leave_Type": "Special Leave",
            "Role": "Student",
            "Leave_Date": "08 May 2024 - 19 may 2024",
            "No_of_Days": "1",
            "Applied_On": "12 May 2024",
            "Authority": "Hellana",
            "Status": "Pending"
        },
        {
            "Submitted_By": "Gifford (7457)",
            "Leave_Type": "Medical Leave",
            "Role": "Student",
            "Leave_Date": "07 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "04 May 2024",
            "Authority": "Erickson",
            "Status": "Pending"
        },
        {
            "Submitted_By": "Julie (4655)",
            "Leave_Type": "Casual Leave",
            "Role": "Student",
            "Leave_Date": "05 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "04 May 2024",
            "Authority": "Raul",
            "Status": "Approved"
        },
        {
            "Submitted_By": "Joann (4178)",
            "Leave_Type": "Medical Leave",
            "Role": "Student",
            "Leave_Date": "08 May 2024 - 19 may 2024",
            "No_of_Days": "1",
            "Applied_On": "04 May 2024",
            "Authority": "Aaron",
            "Status": "Pending"
        },
        {
            "Submitted_By": "Kathleen (5898)",
            "Leave_Type": "Casual Leave",
            "Role": "Student",
            "Leave_Date": "07 May 2024 - 07 may 2024",
            "No_of_Days": "1",
            "Applied_On": "04 May 2024",
            "Authority": "Morgan",
            "Status": "Pending"
        }
    ]
    return render(request, 'pages/hrm/leaves/approve-request.html', {"approve_request" : approve_request})

def holidays(request):
    holidays = [
        {
            "ID": "H752762",
            "Holiday_Title": "New Year",
            "Date": "01 Jan 2024",
            "Description": "First day of the new year",
            "Status": "Active"
        },
        {
            "ID": "H752761",
            "Holiday_Title": "Martin Luther King Jr. Day",
            "Date": "15 Jan 2024",
            "Description": "Celebrating the civil rights leader",
            "Status": "Active"
        },
        {
            "ID": "H752760",
            "Holiday_Title": "Presidents' Day",
            "Date": "19 Feb 2024",
            "Description": "Honoring past US Presidents",
            "Status": "Active"
        },
        {
            "ID": "H752759",
            "Holiday_Title": "Good Friday",
            "Date": "29 Mar 2024",
            "Description": "Holiday before Easter",
            "Status": "Active"
        },
        {
            "ID": "H752758",
            "Holiday_Title": "Easter Monday",
            "Date": "01 Apr 2024",
            "Description": "Holiday after Easter",
            "Status": "Active"
        },
        {
            "ID": "H752757",
            "Holiday_Title": "Memorial Day",
            "Date": "27 May 2024",
            "Description": "Honors military personnel",
            "Status": "Active"
        },
        {
            "ID": "H752756",
            "Holiday_Title": "Independence Day",
            "Date": "04 Jul 2024",
            "Description": "Celebrates Independence",
            "Status": "Active"
        },
        {
            "ID": "H752755",
            "Holiday_Title": "Labor Day",
            "Date": "02 Sep 2024",
            "Description": "Honors working people",
            "Status": "Active"
        },
        {
            "ID": "H752754",
            "Holiday_Title": "Veterans Day",
            "Date": "11 Nov 2024",
            "Description": "Honors military veterans",
            "Status": "Active"
        },
        {
            "ID": "H752753",
            "Holiday_Title": "Christmas Day",
            "Date": "25 Dec 2024",
            "Description": "Celebration of Christmas",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/hrm/holidays.html', {"holidays" : holidays})

def payroll(request):
    payroll = [
        {
            "ID": "P738197",
            "Image": "assets/img/profiles/avatar-27.jpg",
            "Name": "Kevin",
            "Department": "Admin",
            "Designation": "Technical Head",
            "Phone": "+1 63423 72397",
            "Amount": "$15,000",
            "Status": "Paid"
        },
        {
            "ID": "P738197",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Willie",
            "Department": "Management",
            "Designation": "Receptionist",
            "Phone": "+1 82913 61371",
            "Amount": "$12,000",
            "Status": "Generated"
        },
        {
            "ID": "P738196",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Department": "Management",
            "Designation": "Admin",
            "Phone": "+1 56752 86742",
            "Amount": "$13,000",
            "Status": "Paid"
        },
        {
            "ID": "P738195",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Department": "Management",
            "Designation": "Admin",
            "Phone": "+1 82392 37359",
            "Amount": "$13,000",
            "Status": "Paid"
        },
        {
            "ID": "P738194",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Johnson",
            "Department": "Finance",
            "Designation": "Accountant",
            "Phone": "+1 53619 54691",
            "Amount": "$18,000",
            "Status": "Paid"
        },
        {
            "ID": "P738193",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Department": "Management",
            "Designation": "HR Manager",
            "Phone": "+1 23566 52683",
            "Amount": "$12,000",
            "Status": "Generated"
        },
        {
            "ID": "P738192",
            "Image": "assets/img/members/members-01.jpg",
            "Name": "James",
            "Department": "Library",
            "Designation": "Librarian",
            "Phone": "+1 78429 82414",
            "Amount": "$10,000",
            "Status": "Paid"
        },
        {
            "ID": "P738191",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Department": "Transport",
            "Designation": "Driver",
            "Phone": "+1 77502 54845",
            "Amount": "$8000",
            "Status": "Paid"
        },
        {
            "ID": "P738190",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Department": "Finance",
            "Designation": "Accounts Manager",
            "Phone": "+1 56187 87489",
            "Amount": "$12,000",
            "Status": "Paid"
        },
        {
            "ID": "P738189",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Department": "Management",
            "Designation": "Receptionist",
            "Phone": "+1 97846 84518",
            "Amount": "$10,000",
            "Status": "Paid"
        }
    ]
    return render(request, 'pages/hrm/payroll.html', {"payroll" : payroll })

def staff_details(request):
    return render(request, 'pages/hrm/staff-details.html')

def staff_payroll(request):
    return render(request, 'pages/hrm/staff-payroll.html')

def staff_leaves(request):
    return render(request, 'pages/hrm/staff-leaves.html')

def staffs_attendance(request):
    return render(request, 'pages/hrm/staffs-attendance.html')

#  Finance & Accounts

def expenses(request):
    expenses = [
        {
            "ID": "EX628148",
            "Expense_Name": "Monthly Electricity",
            "Description": "Electricity of April month",
            "Category": "Utilities",
            "Date": "25 Apr 2024",
            "Amount": "$1000",
            "Invoice_No": "INV681537",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628147",
            "Expense_Name": "Teacher Salary",
            "Description": "April payroll for teching staffs",
            "Category": "Salaries",
            "Date": "29 Apr 2024",
            "Amount": "$20,000",
            "Invoice_No": "INV681536",
            "Payment_Method": "Credit"
        },
        {
            "ID": "EX628146",
            "Expense_Name": "AC Repair",
            "Description": "Air Conditioning repair",
            "Category": "Maintenance",
            "Date": "11 May 2024",
            "Amount": "$400",
            "Invoice_No": "INV681535",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628145",
            "Expense_Name": "Fuel Expense",
            "Description": "Fuel for school buses",
            "Category": "Transportation",
            "Date": "16 May 2024",
            "Amount": "$1200",
            "Invoice_No": "INV681534",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628144",
            "Expense_Name": "Sports Uniform",
            "Description": "New uniform for soccer team",
            "Category": "Sports",
            "Date": "21 May 2024",
            "Amount": "$2000",
            "Invoice_No": "INV681533",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628143",
            "Expense_Name": "Water Bill",
            "Description": "Monthly water usage bill",
            "Category": "Utilities",
            "Date": "14 Jun 2024",
            "Amount": "$700",
            "Invoice_No": "INV681532",
            "Payment_Method": "Credit"
        },
        {
            "ID": "EX628142",
            "Expense_Name": "Projector purchase",
            "Description": "Projector for auditorium",
            "Category": "Equipment",
            "Date": "20 Jun 2024",
            "Amount": "$600",
            "Invoice_No": "INV681531",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628141",
            "Expense_Name": "Vehicle Repair",
            "Description": "Repairs for school buses",
            "Category": "Transportation",
            "Date": "24 Jun 2024",
            "Amount": "$800",
            "Invoice_No": "INV681530",
            "Payment_Method": "Cash"
        },
        {
            "ID": "EX628140",
            "Expense_Name": "Graduation Setup",
            "Description": "Setup costs for graduation",
            "Category": "Events",
            "Date": "08 Jul 2024",
            "Amount": "$5000",
            "Invoice_No": "INV681529",
            "Payment_Method": "Credit"
        },
        {
            "ID": "EX628139",
            "Expense_Name": "Lab Equipments",
            "Description": "New microscopes for labs",
            "Category": "Equipment",
            "Date": "13 Jul 2024",
            "Amount": "$300",
            "Invoice_No": "INV681537",
            "Payment_Method": "Cash"
        }
    ]
    return render(request, 'pages/finance-accounts/expenses.html', {"expenses" : expenses })

def expenses_category(request):
    expenses_category = [
        {
            "ID": "EXC617453",
            "Category": "Utilities",
            "Description": "Expenses related to electricity, water, and gas"
        },
        {
            "ID": "EXC617452",
            "Category": "Salaries",
            "Description": "Monthly payment for teaching and non-teaching staff"
        },
        {
            "ID": "EXC617451",
            "Category": "Maintenance",
            "Description": "Costs for maintaining and repairing school property"
        },
        {
            "ID": "EXC617450",
            "Category": "Transportation",
            "Description": "Expenses for school transportation services"
        },
        {
            "ID": "EXC617449",
            "Category": "Sports",
            "Description": "Expenses for sports equipment and team uniforms"
        },
        {
            "ID": "EXC617448",
            "Category": "Office Supplies",
            "Description": "Regular purchases of stationery and office supplies"
        },
        {
            "ID": "EXC617447",
            "Category": "Equipment",
            "Description": "Purchase of educational and administrative equipment"
        },
        {
            "ID": "EXC617446",
            "Category": "Technology",
            "Description": "Investment in software, hardware, and IT support"
        },
        {
            "ID": "EXC617445",
            "Category": "Events",
            "Description": "Costs associated with organizing school events"
        },
        {
            "ID": "EXC617444",
            "Category": "Food Services",
            "Description": "Expenses for cafeteria services and food supplies"
        }
    ]
    return render(request, 'pages/finance-accounts/expenses-category.html', {"expenses_category" : expenses_category})

def accounts_income(request):
    accounts_income = [
        {
            "ID": "I639248",
            "Income_Name": "April Month Fees",
            "Description": "Tuition for Term 1, Class II",
            "Source": "Tuition Fees",
            "Date": "25 Apr 2024",
            "Amount": "$15,000",
            "Invoice_No": "INV681537",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639247",
            "Income_Name": "STEM Program Grant",
            "Description": "Annual funding for STEM programs",
            "Source": "Government Grants",
            "Date": "29 Apr 2024",
            "Amount": "$20,000",
            "Invoice_No": "INV681536",
            "Payment_Method": "Credit"
        },
        {
            "ID": "I639246",
            "Income_Name": "Alumni Scholarship",
            "Description": "Donation from Alumni for scholarships",
            "Source": "Donations",
            "Date": "11 May 2024",
            "Amount": "$1000",
            "Invoice_No": "INV681535",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639245",
            "Income_Name": "Uniform Sales",
            "Description": "Sale of school uniforms",
            "Source": "Merchandise",
            "Date": "16 May 2024",
            "Amount": "$10,500",
            "Invoice_No": "INV681534",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639244",
            "Income_Name": "Event Parking Fees",
            "Description": "Monthly parking fees for external users",
            "Source": "Parking Fees",
            "Date": "21 May 2024",
            "Amount": "$8000",
            "Invoice_No": "INV681533",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639243",
            "Income_Name": "Football Season Pass",
            "Description": "Season passes for school football games",
            "Source": "Sports",
            "Date": "14 Jun 2024",
            "Amount": "$7000",
            "Invoice_No": "INV681532",
            "Payment_Method": "Credit"
        },
        {
            "ID": "I639242",
            "Income_Name": "Summer Reading Sale",
            "Description": "Sales from summer reading book fair",
            "Source": "Book Fair",
            "Date": "20 Jun 2024",
            "Amount": "$3000",
            "Invoice_No": "INV681531",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639241",
            "Income_Name": "Library Donation",
            "Description": "Funds donated for library improvements",
            "Source": "Donations",
            "Date": "24 Jun 2024",
            "Amount": "$2000",
            "Invoice_No": "INV681530",
            "Payment_Method": "Cash"
        },
        {
            "ID": "I639240",
            "Income_Name": "Cafeteria Income",
            "Description": "Monthly Cafeteria Income",
            "Source": "Cafeteria",
            "Date": "08 Jul 2024",
            "Amount": "$15,000",
            "Invoice_No": "INV681529",
            "Payment_Method": "Credit"
        },
        {
            "ID": "I639239",
            "Income_Name": "Daily Visitor Parking",
            "Description": "Parking fees collected from visitors",
            "Source": "Parking Fees",
            "Date": "13 Jul 2024",
            "Amount": "$4000",
            "Invoice_No": "INV681537",
            "Payment_Method": "Cash"
        }
    ]
    return render(request, 'pages/finance-accounts/accounts-income.html', {"accounts_income" : accounts_income})

def accounts_invoices(request):
    accounts_invoices = [
        {
            "Invoice_Number": "INV681537",
            "Date": "25 Apr 2024",
            "Description": "April Month Fees",
            "Amount": "$15,000",
            "Payment_Method": "Cash",
            "Due_Date": "30 Apr 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681536",
            "Date": "29 Apr 2024",
            "Description": "STEM Program Grant",
            "Amount": "$20,000",
            "Payment_Method": "Credit",
            "Due_Date": "05 May 2024",
            "Status": "Overdue"
        },
        {
            "Invoice_Number": "INV681535",
            "Date": "11 May 2024",
            "Description": "Alumni Scholarship",
            "Amount": "$1000",
            "Payment_Method": "Cash",
            "Due_Date": "16 May 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681534",
            "Date": "16 May 2024",
            "Description": "Uniform Sales",
            "Amount": "$10,500",
            "Payment_Method": "Cash",
            "Due_Date": "21 May 2024",
            "Status": "Pending"
        },
        {
            "Invoice_Number": "INV681533",
            "Date": "21 May 2024",
            "Description": "Event Parking Fees",
            "Amount": "$8000",
            "Payment_Method": "Cash",
            "Due_Date": "26 May 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681532",
            "Date": "14 Jun 2024",
            "Description": "Football Season Pass",
            "Amount": "$7000",
            "Payment_Method": "Credit",
            "Due_Date": "19 Jun 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681531",
            "Date": "20 Jun 2024",
            "Description": "Summer Reading Sale",
            "Amount": "$3000",
            "Payment_Method": "Cash",
            "Due_Date": "25 Jun 2024",
            "Status": "Overdue"
        },
        {
            "Invoice_Number": "INV681530",
            "Date": "24 Jun 2024",
            "Description": "Library Donation",
            "Amount": "$2000",
            "Payment_Method": "Cash",
            "Due_Date": "29 Jun 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681529",
            "Date": "08 Jul 2024",
            "Description": "Cafeteria Income",
            "Amount": "$15,000",
            "Payment_Method": "Credit",
            "Due_Date": "13 Jul 2024",
            "Status": "Paid"
        },
        {
            "Invoice_Number": "INV681537",
            "Date": "13 Jul 2024",
            "Description": "Daily Visitor Parking",
            "Amount": "$4000",
            "Payment_Method": "Cash",
            "Due_Date": "18 Jul 2024",
            "Status": "Pending"
        }
    ]
    return render(request, 'pages/finance-accounts/accounts-invoices.html', {"accounts_invoices" : accounts_invoices})

def invoice(request):
    return render(request, 'pages/finance-accounts/invoice.html')

def accounts_transactions(request):
    accounts_transactions = [
        {
            "ID": "FT624893",
            "Description": "April Month Fees",
            "Transaction_Date": "25 Apr 2024",
            "Amount": "$15,000",
            "Transaction_Type": "Income",
            "Payment_Method": "Cash",
            "Status": "Completed"
        },
        {
            "ID": "FT624892",
            "Description": "Monthly Electricity",
            "Transaction_Date": "27 Apr 2024",
            "Amount": "$1000",
            "Transaction_Type": "Expense",
            "Payment_Method": "Credit",
            "Status": "Completed"
        },
        {
            "ID": "FT624891",
            "Description": "Alumni Scholarship",
            "Transaction_Date": "03 May 2024",
            "Amount": "$1000",
            "Transaction_Type": "Income",
            "Payment_Method": "Cash",
            "Status": "Pending"
        },
        {
            "ID": "FT624890",
            "Description": "AC Repair",
            "Transaction_Date": "15 May 2024",
            "Amount": "$400",
            "Transaction_Type": "Expense",
            "Payment_Method": "Cash",
            "Status": "Completed"
        },
        {
            "ID": "FT624889",
            "Description": "Uniform Sales",
            "Transaction_Date": "20 May 2024",
            "Amount": "$10,500",
            "Transaction_Type": "Income",
            "Payment_Method": "Credit",
            "Status": "Completed"
        },
        {
            "ID": "FT624888",
            "Description": "Water Bill",
            "Transaction_Date": "06 Jun 2024",
            "Amount": "$700",
            "Transaction_Type": "Expense",
            "Payment_Method": "Cash",
            "Status": "Pending"
        },
        {
            "ID": "FT624887",
            "Description": "Library Donation",
            "Transaction_Date": "18 Jun 2024",
            "Amount": "$2,000",
            "Transaction_Type": "Income",
            "Payment_Method": "Cash",
            "Status": "Completed"
        },
        {
            "ID": "FT624886",
            "Description": "Vehicle Repair",
            "Transaction_Date": "26 Jun 2024",
            "Amount": "$800",
            "Transaction_Type": "Expense",
            "Payment_Method": "Cash",
            "Status": "Completed"
        },
        {
            "ID": "FT624885",
            "Description": "Cafeteria Income",
            "Transaction_Date": "08 Jul 2024",
            "Amount": "$15,000",
            "Transaction_Type": "Income",
            "Payment_Method": "Credit",
            "Status": "Completed"
        },
        {
            "ID": "FT624884",
            "Description": "Lab Equipments",
            "Transaction_Date": "10 Jul 2024",
            "Amount": "$300",
            "Transaction_Type": "Expense",
            "Payment_Method": "Cash",
            "Status": "Completed"
        }
    ]
    return render(request, 'pages/finance-accounts/accounts-transactions.html', {"accounts_transactions" : accounts_transactions})

def add_invoice(request):
    return render(request, 'pages/finance-accounts/add-invoice.html')

def edit_invoice(request):
    return render(request, 'pages/finance-accounts/edit-invoice.html')


# Announcements

def notice_board(request):
    return render(request, 'pages/announcements/notice-board.html')

def events(request):
    return render(request, 'pages/announcements/events.html')


# Reports

def attendance_report(request):
    return render(request, 'pages/reports/attendance/attendance-report.html')

def student_attendance_type(request):
    student_attendance_type = [
        {
            "Admission_No": "AD9892434",
            "Date_of_Admission": "25 Mar 2024",
            "Student_Name": "Janet",
            "Student_Img": "assets/img/students/student-01.jpg",
            "Class": "III",
            "Date_of_Birth": "10 Jan 2015",
            "Father_Name": "Mary",
            "Father_Img": "assets/img/parents/parent-10.jpg",
            "Count": "22"
        },
        {
            "Admission_No": "AD9892433",
            "Date_of_Admission": "18 Mar 2024",
            "Student_Name": "Joann",
            "Student_Img": "assets/img/students/student-02.jpg",
            "Class": "IV",
            "Date_of_Birth": "19 Aug 2014",
            "Father_Name": "Michael",
            "Father_Img": "assets/img/parents/parent-09.jpg",
            "Count": "15"
        },
        {
            "Admission_No": "AD9892432",
            "Date_of_Admission": "14 Mar 2024",
            "Student_Name": "Kathleen",
            "Student_Img": "assets/img/students/student-03.jpg",
            "Class": "II",
            "Date_of_Birth": "05 Dec 2017",
            "Father_Name": "Jessie",
            "Father_Img": "assets/img/parents/parent-08.jpg",
            "Count": "24"
        },
        {
            "Admission_No": "AD9892431",
            "Date_of_Admission": "27 Feb 2024",
            "Student_Name": "Gifford",
            "Student_Img": "assets/img/students/student-04.jpg",
            "Class": "I",
            "Date_of_Birth": "22 Mar 2018",
            "Father_Name": "Robert",
            "Father_Img": "assets/img/parents/parent-07.jpg",
            "Count": "22"
        },
        {
            "Admission_No": "AD9892430",
            "Date_of_Admission": "13 Feb 2024",
            "Student_Name": "Gifford",
            "Student_Img": "assets/img/students/student-05.jpg",
            "Class": "II",
            "Date_of_Birth": "13 May 2017",
            "Father_Name": "Colleen",
            "Father_Img": "assets/img/parents/parent-06.jpg",
            "Count": "22"
        },
        {
            "Admission_No": "AD9892429",
            "Date_of_Admission": "11 Feb 2024",
            "Student_Name": "Ralph",
            "Student_Img": "assets/img/students/student-06.jpg",
            "Class": "III",
            "Date_of_Birth": "20 Jun 2015",
            "Father_Name": "Arthur",
            "Father_Img": "assets/img/parents/parent-05.jpg",
            "Count": "24"
        },
        {
            "Admission_No": "AD9892428",
            "Date_of_Admission": "24 Jan 2024",
            "Student_Name": "Julie",
            "Student_Img": "assets/img/students/student-07.jpg",
            "Class": "V",
            "Date_of_Birth": "18 Sep 2013",
            "Father_Name": "Claudia",
            "Father_Img": "assets/img/parents/parent-04.jpg",
            "Count": "24"
        },
        {
            "Admission_No": "AD9892427",
            "Date_of_Admission": "19 Jan 2024",
            "Student_Name": "Ryan",
            "Student_Img": "assets/img/students/student-08.jpg",
            "Class": "VI",
            "Date_of_Birth": "26 Nov 2012",
            "Father_Name": "Johnson",
            "Father_Img": "assets/img/parents/parent-03.jpg",
            "Count": "21"
        },
        {
            "Admission_No": "AD9892426",
            "Date_of_Admission": "08 Jan 2024",
            "Student_Name": "Susan",
            "Student_Img": "assets/img/students/student-09.jpg",
            "Class": "VIII",
            "Date_of_Birth": "26 May 2010",
            "Father_Name": "Marquita",
            "Father_Img": "assets/img/parents/parent-02.jpg",
            "Count": "24"
        },
        {
            "Admission_No": "AD9892425",
            "Date_of_Admission": "22 Dec 2024",
            "Student_Name": "Richard",
            "Student_Img": "assets/img/students/student-10.jpg",
            "Class": "VII",
            "Date_of_Birth": "06 Oct 2011",
            "Father_Name": "Thomas",
            "Father_Img": "assets/img/parents/parent-01.jpg",
            "Count": "24"
        },
        {
            "Admission_No": "AD9892424",
            "Date_of_Admission": "15 Dec 2024",
            "Student_Name": "Veronica",
            "Student_Img": "assets/img/students/student-11.jpg",
            "Class": "IX",
            "Date_of_Birth": "27 Dec 2009",
            "Father_Name": "Jessie",
            "Father_Img": "assets/img/parents/parent-14.jpg",
            "Count": "24"
        }
    ]
    return render(request, 'pages/reports/attendance/student-attendance-type.html', {"student_attendance_type" : student_attendance_type})

def daily_attendance(request):
    daily_attendance = [
        {
            "Class": "III",
            "Section": "A",
            "Total_Present": "69",
            "Total_Absent": "2",
            "Present": "98%",
            "Absent": "2%"
        },
        {
            "Class": "IV",
            "Section": "A",
            "Total_Present": "45",
            "Total_Absent": "7",
            "Present": "78%",
            "Absent": "22%"
        },
        {
            "Class": "II",
            "Section": "B",
            "Total_Present": "69",
            "Total_Absent": "8",
            "Present": "89%",
            "Absent": "11%"
        },
        {
            "Class": "I",
            "Section": "C",
            "Total_Present": "54",
            "Total_Absent": "7",
            "Present": "98%",
            "Absent": "1%"
        },
        {
            "Class": "II",
            "Section": "A",
            "Total_Present": "65",
            "Total_Absent": "1",
            "Present": "98%",
            "Absent": "2%"
        },
        {
            "Class": "III",
            "Section": "B",
            "Total_Present": "78",
            "Total_Absent": "2",
            "Present": "72%",
            "Absent": "28%"
        },
        {
            "Class": "V",
            "Section": "C",
            "Total_Present": "65",
            "Total_Absent": "0",
            "Present": "100%",
            "Absent": "0%"
        },
        {
            "Class": "VI",
            "Section": "A",
            "Total_Present": "45",
            "Total_Absent": "2",
            "Present": "98%",
            "Absent": "1%"
        },
        {
            "Class": "VIII",
            "Section": "B",
            "Total_Present": "47",
            "Total_Absent": "2",
            "Present": "98%",
            "Absent": "2%"
        },
        {
            "Class": "VII",
            "Section": "C",
            "Total_Present": "45",
            "Total_Absent": "7",
            "Present": "89%",
            "Absent": "11%"
        },
        {
            "Class": "IX",
            "Section": "A",
            "Total_Present": "45",
            "Total_Absent": "1",
            "Present": "98%",
            "Absent": "2%"
        }
    ]
    return render(request, 'pages/reports/attendance/daily-attendance.html', {"daily_attendance" : daily_attendance})

def student_day_wise(request):
    student_day_wise = [
        {
            "S_No": "1",
            "Image": "assets/img/students/student-01.jpg",
            "Admission_No": "AD9892434",
            "Roll_No": "35013",
            "Name": "Janet",
            "Attendance": "Present"
        },
        {
            "S_No": "2",
            "Image": "assets/img/students/student-02.jpg",
            "Admission_No": "AD9892433",
            "Roll_No": "35012",
            "Name": "Joann",
            "Attendance": "Present"
        },
        {
            "S_No": "3",
            "Image": "assets/img/students/student-03.jpg",
            "Admission_No": "AD9892432",
            "Roll_No": "35011",
            "Name": "Kathleen",
            "Attendance": "Half Day"
        },
        {
            "S_No": "4",
            "Image": "assets/img/students/student-04.jpg",
            "Admission_No": "AD9892431",
            "Roll_No": "35010",
            "Name": "Gifford",
            "Attendance": "Present"
        },
        {
            "S_No": "5",
            "Image": "assets/img/students/student-05.jpg",
            "Admission_No": "AD9892430",
            "Roll_No": "35009",
            "Name": "Lisa",
            "Attendance": "Absent"
        },
        {
            "S_No": "6",
            "Image": "assets/img/students/student-06.jpg",
            "Admission_No": "AD9892429",
            "Roll_No": "35008",
            "Name": "Ralph",
            "Attendance": "Late"
        },
        {
            "S_No": "7",
            "Image": "assets/img/students/student-07.jpg",
            "Admission_No": "AD9892428",
            "Roll_No": "35007",
            "Name": "Julie",
            "Attendance": "Present"
        },
        {
            "S_No": "8",
            "Image": "assets/img/students/student-08.jpg",
            "Admission_No": "AD9892427",
            "Roll_No": "35006",
            "Name": "Ryan",
            "Attendance": "Present"
        },
        {
            "S_No": "9",
            "Image": "assets/img/students/student-09.jpg",
            "Admission_No": "AD9892426",
            "Roll_No": "35005",
            "Name": "Susan",
            "Attendance": "Absent"
        },
        {
            "S_No": "10",
            "Image": "assets/img/students/student-10.jpg",
            "Admission_No": "AD9892425",
            "Roll_No": "35004",
            "Name": "Richard",
            "Attendance": "Present"
        }
    ]
    return render(request, 'pages/reports/attendance/student-day-wise.html', {"student_day_wise" : student_day_wise})

def teacher_day_wise(request):
    teacher_day_wise = [
        {
            "S_No": "1",
            "ID": "T849127",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Subject": "Physics",
            "Attendance": "Present"
        },
        {
            "S_No": "2",
            "ID": "T849126",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Subject": "Computer",
            "Attendance": "Present"
        },
        {
            "S_No": "3",
            "ID": "T849125",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Subject": "English",
            "Attendance": "Absent"
        },
        {
            "S_No": "4",
            "ID": "T849124",
            "Image": "assets/img/teachers/teacher-04.jpg",
            "Name": "Erickson",
            "Subject": "Spanish",
            "Attendance": "Present"
        },
        {
            "S_No": "5",
            "ID": "T849123",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Morgan",
            "Subject": "Env Science",
            "Attendance": "Half Day"
        },
        {
            "S_No": "6",
            "ID": "T849122",
            "Image": "assets/img/teachers/teacher-06.jpg",
            "Name": "Aaron",
            "Subject": "Chemistry",
            "Attendance": "Present"
        },
        {
            "S_No": "7",
            "ID": "T849121",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Subject": "Maths",
            "Attendance": "Present"
        },
        {
            "S_No": "8",
            "ID": "T849120",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Raul",
            "Subject": "Biology",
            "Attendance": "Late"
        },
        {
            "S_No": "9",
            "ID": "T849119",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Subject": "Economics",
            "Attendance": "Present"
        },
        {
            "S_No": "10",
            "ID": "T849118",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Subject": "Finance",
            "Attendance": "Present"
        }
    ]
    return render(request, 'pages/reports/attendance/teacher-day-wise.html', {"teacher_day_wise" : teacher_day_wise })

def teacher_report(request):
    return render(request, 'pages/reports/attendance/teacher-report.html')

def staff_day_wise(request):
    staff_day_wise = [
        {
            "S_No": "1",
            "ID": "8483",
            "Image": "assets/img/teachers/teacher-03.jpg",
            "Name": "Hellana",
            "Department": "Management",
            "Role": "Receptionist",
            "Attendance": "Present"
        },
        {
            "S_No": "2",
            "ID": "8482",
            "Image": "assets/img/teachers/teacher-02.jpg",
            "Name": "Daniel",
            "Department": "Finance",
            "Role": "Accounts Manager",
            "Attendance": "Present"
        },
        {
            "S_No": "3",
            "ID": "8481",
            "Image": "assets/img/profiles/avatar-27.jpg",
            "Name": "Kevin",
            "Department": "Management",
            "Role": "Driver",
            "Attendance": "Absent"
        },
        {
            "S_No": "4",
            "ID": "8480",
            "Image": "assets/img/teachers/teacher-01.jpg",
            "Name": "Teresa",
            "Department": "Finance",
            "Role": "Librarian",
            "Attendance": "Present"
        },
        {
            "S_No": "5",
            "ID": "8479",
            "Image": "assets/img/members/members-01.jpg",
            "Name": "James",
            "Department": "Management",
            "Role": "HR Manager",
            "Attendance": "Half Day"
        },
        {
            "S_No": "6",
            "ID": "8478",
            "Image": "assets/img/teachers/teacher-08.jpg",
            "Name": "Johnson",
            "Department": "Admin",
            "Role": "Accountant",
            "Attendance": "Present"
        },
        {
            "S_No": "7",
            "ID": "8477",
            "Image": "assets/img/teachers/teacher-10.jpg",
            "Name": "Edward",
            "Department": "Transport",
            "Role": "Admin",
            "Attendance": "Present"
        },
        {
            "S_No": "8",
            "ID": "8476",
            "Image": "assets/img/teachers/teacher-07.jpg",
            "Name": "Jacquelin",
            "Department": "Library",
            "Role": "Admin",
            "Attendance": "Late"
        },
        {
            "S_No": "9",
            "ID": "8475",
            "Image": "assets/img/teachers/teacher-09.jpg",
            "Name": "Elizabeth",
            "Department": "Management",
            "Role": "Receptionist",
            "Attendance": "Present"
        },
        {
            "S_No": "10",
            "ID": "8474",
            "Image": "assets/img/teachers/teacher-05.jpg",
            "Name": "Willie",
            "Department": "Management",
            "Role": "Technical Head",
            "Attendance": "Present"
        }
    ]
    return render(request, 'pages/reports/attendance/staff-day-wise.html', {"staff_day_wise" : staff_day_wise})

def staff_report(request):
    return render(request, 'pages/reports/attendance/staff-report.html')

def class_report(request):
    class_report = [
        {
            "ID": "C138038",
            "Class": "I",
            "Section": "A",
            "Students": "30",
        },
        {
            "ID": "C138037",
            "Class": "I",
            "Section": "B",
            "Students": "25",
        },
        {
            "ID": "C138036",
            "Class": "II",
            "Section": "A",
            "Students": "40",
        },
        {
            "ID": "C138035",
            "Class": "II",
            "Section": "B",
            "Students": "35",
        },
        {
            "ID": "C138034",
            "Class": "II",
            "Section": "C",
            "Students": "25",
        },
        {
            "ID": "C138033",
            "Class": "III",
            "Section": "A",
            "Students": "30",
        },
        {
            "ID": "C138032",
            "Class": "III",
            "Section": "B",
            "Students": "25",
        },
        {
            "ID": "C138031",
            "Class": "IV",
            "Section": "A",
            "Students": "20",
        },
        {
            "ID": "C138030",
            "Class": "IV",
            "Section": "B",
            "Students": "30",
        },
        {
            "ID": "C138029",
            "Class": "V",
            "Section": "A",
            "Students": "35"
        }
    ]
    return render(request, 'pages/reports/class-report.html', {"class_report" : class_report})

def student_report(request):
    student_report = [
        {
            "Admission_No": "AD9892434",
            "Roll_No": "35013",
            "Name": "Janet",
            "Student_Img": "assets/img/students/student-01.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Female",
            "Parent": "Thomas",
            "Parent_Img": "assets/img/profiles/avatar-02.jpg",
            "Date_of_Join": "25 Mar 2024",
            "DOB": "10 Jan 2015",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892433",
            "Roll_No": "35012",
            "Name": "Joann",
            "Student_Img": "assets/img/students/student-02.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Male",
            "Parent": "Marquita",
            "Parent_Img": "assets/img/profiles/avatar-01.jpg",
            "Date_of_Join": "18 Mar 2024",
            "DOB": "19 Aug 2014",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892432",
            "Roll_No": "35011",
            "Name": "Kathleen",
            "Student_Img": "assets/img/students/student-03.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Female",
            "Parent": "Johnson",
            "Parent_Img": "assets/img/parents/parent-03.jpg",
            "Date_of_Join": "14 Mar 2024",
            "DOB": "05 Dec 2017",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892431",
            "Roll_No": "35010",
            "Name": "Gifford",
            "Student_Img": "assets/img/students/student-04.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Male",
            "Parent": "Claudia",
            "Parent_Img": "assets/img/parents/parent-04.jpg",
            "Date_of_Join": "27 Feb 2024",
            "DOB": "22 Mar 2018",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892430",
            "Roll_No": "35009",
            "Name": "Lisa",
            "Student_Img": "assets/img/students/student-05.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Female",
            "Parent": "Arthur",
            "Parent_Img": "assets/img/parents/parent-05.jpg",
            "Date_of_Join": "13 Feb 2024",
            "DOB": "13 May 2017",
            "Status": "Inactive"
        },
        {
            "Admission_No": "AD9892429",
            "Roll_No": "35008",
            "Name": "Lisa",
            "Student_Img": "assets/img/students/student-06.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Male",
            "Parent": "Colleen",
            "Parent_Img": "assets/img/parents/parent-06.jpg",
            "Date_of_Join": "11 Feb 2024",
            "DOB": "20 Jun 2015",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892428",
            "Roll_No": "35007",
            "Name": "Julie",
            "Student_Img": "assets/img/students/student-07.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Female",
            "Parent": "Robert",
            "Parent_Img": "assets/img/parents/parent-07.jpg",
            "Date_of_Join": "24 Jan 2024",
            "DOB": "18 Sep 2013",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892427",
            "Roll_No": "35006",
            "Name": "Ryan",
            "Student_Img": "assets/img/students/student-08.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Male",
            "Parent": "Jessie",
            "Parent_Img": "assets/img/parents/parent-08.jpg",
            "Date_of_Join": "19 Jan 2024",
            "DOB": "26 Nov 2012",
            "Status": "Active"
        },
        {
            "Admission_No": "AD9892426",
            "Roll_No": "35005",
            "Name": "Susan",
            "Student_Img": "assets/img/students/student-09.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Female",
            "Parent": "Michael",
            "Parent_Img": "assets/img/parents/parent-09.jpg",
            "Date_of_Join": "08 Jan 2024",
            "DOB": "26 May 2010",
            "Status": "Inactive"
        },
        {
            "Admission_No": "AD9892425",
            "Roll_No": "35004",
            "Name": "Richard",
            "Student_Img": "assets/img/students/student-10.jpg",
            "Class": "I",
            "Section": "A",
            "Gender": "Male",
            "Parent": "Mary",
            "Parent_Img": "assets/img/parents/parent-10.jpg",
            "Date_of_Join": "22 Dec 2024",
            "DOB": "06 Oct 2011",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/reports/student-report.html', {"student_report" : student_report })

def grade_report(request):
    grade_report = [
        {
            "Admission_No": "AD9892434",
            "Student_Name": "Janet",
            "Image": "assets/img/students/student-01.jpg",
            "Roll_No" : "35013",
            "English": "95",
            "Spanish": "93",
            "Physics": "88",
            "Chemistry": "90",
            "Maths": "85",
            "Computer": "98",
            "Env_Science": "95",
            "Total": "644",
            "Percent": "92",
            "Grade": "O"
        },
        {
            "Admission_No": "AD9892433",
            "Student_Name": "Joann",
            "Image": "assets/img/students/student-02.jpg",
            "Roll_No" : "35012",
            "English": "30",
            "Spanish": "35",
            "Physics": "36",
            "Chemistry": "28",
            "Maths": "38",
            "Computer": "40",
            "Env_Science": "37",
            "Total": "244",
            "Percent": "34",
            "Grade": "F"
        },
        {
            "Admission_No": "AD9892432",
            "Student_Name": "Kathleen",
            "Image": "assets/img/students/student-03.jpg",
            "Roll_No" : "35011",
            "English": "70",
            "Spanish": "80",
            "Physics": "85",
            "Chemistry": "78",
            "Maths": "82",
            "Computer": "83",
            "Env_Science": "80",
            "Total": "558",
            "Percent": "79",
            "Grade": "A"
        },
        {
            "Admission_No": "AD9892431",
            "Student_Name": "Gifford",
            "Image": "assets/img/students/student-04.jpg",
            "Roll_No" : "35010",
            "English": "60",
            "Spanish": "68",
            "Physics": "65",
            "Chemistry": "70",
            "Maths": "67",
            "Computer": "72",
            "Env_Science": "75",
            "Total": "477",
            "Percent": "68",
            "Grade": "B+"
        },
        {
            "Admission_No": "AD9892430",
            "Student_Name": "Lisa",
            "Image": "assets/img/students/student-05.jpg",
            "Roll_No" : "35009",
            "English": "36",
            "Spanish": "30",
            "Physics": "40",
            "Chemistry": "38",
            "Maths": "50",
            "Computer": "48",
            "Env_Science": "43",
            "Total": "285",
            "Percent": "40",
            "Grade": "F"
        },
        {
            "Admission_No": "AD9892429",
            "Student_Name": "Ralph",
            "Image": "assets/img/students/student-06.jpg",
            "Roll_No" : "35008",
            "English": "43",
            "Spanish": "50",
            "Physics": "62",
            "Chemistry": "70",
            "Maths": "65",
            "Computer": "58",
            "Env_Science": "60",
            "Total": "408",
            "Percent": "58",
            "Grade": "B"
        },
        {
            "Admission_No": "AD9892428",
            "Student_Name": "Julie",
            "Image": "assets/img/students/student-07.jpg",
            "Roll_No" : "35007",
            "English": "72",
            "Spanish": "80",
            "Physics": "75",
            "Chemistry": "78",
            "Maths": "84",
            "Computer": "87",
            "Env_Science": "76",
            "Total": "552",
            "Percent": "78",
            "Grade": "A"
        },
        {
            "Admission_No": "AD9892427",
            "Student_Name": "Ryan",
            "Image": "assets/img/students/student-08.jpg",
            "Roll_No" : "35006",
            "English": "40",
            "Spanish": "48",
            "Physics": "42",
            "Chemistry": "47",
            "Maths": "32",
            "Computer": "58",
            "Env_Science": "50",
            "Total": "317",
            "Percent": "45",
            "Grade": "F"
        },
        {
            "Admission_No": "AD9892426",
            "Student_Name": "Susan",
            "Image": "assets/img/students/student-09.jpg",
            "Roll_No" : "35004",
            "English": "60",
            "Spanish": "62",
            "Physics": "65",
            "Chemistry": "70",
            "Maths": "72",
            "Computer": "63",
            "Env_Science": "78",
            "Total": "470",
            "Percent": "67",
            "Grade": "B+"
        },
        {
            "Admission_No": "AD9892425",
            "Student_Name": "Richard",
            "Image": "assets/img/students/student-10.jpg",
            "Roll_No" : "35003",
            "English": "72",
            "Spanish": "78",
            "Physics": "85",
            "Chemistry": "83",
            "Maths": "86",
            "Computer": "90",
            "Env_Science": "92",
            "Total": "586",
            "Percent": "83",
            "Grade": "A+"
        }
    ]
    return render(request, 'pages/reports/grade-report.html', {"grade_report" : grade_report })

def leave_report(request):
    return render(request, 'pages/reports/leave-report.html', {"leave_report" : leave_report})

def fees_report(request):
    fees_report = [
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Admission Fees)",
            "Fees_Code": "admission-fees",
            "Due_Date": "25 Mar 2024",
            "Amount": "2000",
            "Status": "Paid",
            "Ref_ID": "#435454",
            "Mode": "Cash",
            "Date_Paid": "25 Jan 2024",
            "Discount": "10%",
            "Fine": "200",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Mar month fees)",
            "Fees_Code": "mar-month-fees",
            "Due_Date": "10 Apr 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435453",
            "Mode": "Cash",
            "Date_Paid": "03 Apr 2024",
            "Discount": "10%",
            "Fine": "0",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Apr month Fees)",
            "Fees_Code": "apr-month-fees",
            "Due_Date": "10 May 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435453",
            "Mode": "Cash",
            "Date_Paid": "03 Apr 2024",
            "Discount": "10%",
            "Fine": "0",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(May month Fees)",
            "Fees_Code": "may-month-fees",
            "Due_Date": "10 Jun 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435451",
            "Mode": "Cash",
            "Date_Paid": "02 Jun 2024",
            "Discount": "10%",
            "Fine": "200",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Jun month Fees)",
            "Fees_Code": "jun-month-fees",
            "Due_Date": "10 Jul 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435450",
            "Mode": "Cash",
            "Date_Paid": "05 Jul 2024",
            "Discount": "10%",
            "Fine": "200",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Jul month Fees)",
            "Fees_Code": "jul-month-fees",
            "Due_Date": "10 Aug 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435449",
            "Mode": "Cash",
            "Date_Paid": "01 Aug 2024",
            "Discount": "10%",
            "Fine": "200",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Dec month Fees)",
            "Fees_Code": "dec-month-fees",
            "Due_Date": "10 Jan 2024",
            "Amount": "2500",
            "Status": "Paid",
            "Ref_ID": "#435443",
            "Mode": "Cash",
            "Date_Paid": "05 Jan 2024",
            "Discount": "10%",
            "Fine": "0",
            "Balance": "0"
        },
        {
            "Fees_Group": "Class 1 General",
            "Fees_Month": "(Jan month Fees)",
            "Fees_Code": "jan-month-fees",
            "Due_Date": "10 Feb 2024",
            "Amount": "2000",
            "Status": "Paid",
            "Ref_ID": "#435443",
            "Mode": "Cash",
            "Date_Paid": "01 Feb 2024",
            "Discount": "10%",
            "Fine": "200",
            "Balance": "0"
        },
        {
            "Fees_Group": "",
            "Fees_Code": "",
            "Due_Date": "",
            "Amount": "2000",
            "Status": "",
            "Ref_ID": "",
            "Mode": "",
            "Date_Paid": "",
            "Discount": "200",
            "Fine": "200",
            "Balance": "0"
        }
    ]
    return render(request, 'pages/reports/fees-report.html', {"fees_report" : fees_report})

# User Management

def users(request):
    users = [
        {
            "ID": "U461893",
            "Name": "Janet",
            "Image": "assets/img/students/student-01.jpg",
            "Class": "III",
            "Section": "A",
            "Date_of_Joined": "25 Mar 2024",
            "Status": "Active"
        },
        {
            "ID": "U461892",
            "Name": "Joann",
            "Image": "assets/img/students/student-02.jpg",
            "Class": "IV",
            "Section": "B",
            "Date_of_Joined": "18 Mar 2024",
            "Status": "Active"
        },
        {
            "ID": "U461891",
            "Name": "Kathleen",
            "Image": "assets/img/students/student-03.jpg",
            "Class": "II",
            "Section": "A",
            "Date_of_Joined": "14 Mar 2024",
            "Status": "Active"
        },
        {
            "ID": "U461890",
            "Name": "Gifford",
            "Image": "assets/img/students/student-04.jpg",
            "Class": "I",
            "Section": "B",
            "Date_of_Joined": "27 Feb 2024",
            "Status": "Active"
        },
        {
            "ID": "U461889",
            "Name": "Lisa",
            "Image": "assets/img/students/student-05.jpg",
            "Class": "II",
            "Section": "B",
            "Date_of_Joined": "13 Feb 2024",
            "Status": "Active"
        },
        {
            "ID": "U461888",
            "Name": "Ralph",
            "Image": "assets/img/students/student-06.jpg",
            "Class": "III",
            "Section": "B",
            "Date_of_Joined": "11 Feb 2024",
            "Status": "Active"
        },
        {
            "ID": "U461887",
            "Name": "Julie",
            "Image": "assets/img/students/student-07.jpg",
            "Class": "V",
            "Section": "A",
            "Date_of_Joined": "24 Jan 2024",
            "Status": "Active"
        },
        {
            "ID": "U461886",
            "Name": "Ryan",
            "Image": "assets/img/students/student-08.jpg",
            "Class": "VI",
            "Section": "A",
            "Date_of_Joined": "19 Jan 2024",
            "Status": "Active"
        },
        {
            "ID": "U461885",
            "Name": "Susan",
            "Image": "assets/img/students/student-09.jpg",
            "Class": "VIII",
            "Section": "B",
            "Date_of_Joined": "08 Jan 2024",
            "Status": "Active"
        },
        {
            "ID": "U461884",
            "Name": "Richard",
            "Image": "assets/img/students/student-12.jpg",
            "Class": "VII",
            "Section": "B",
            "Date_of_Joined": "22 Dec 2024",
            "Status": "Active"
        }
    ]
    return render(request, 'pages/user-management/users.html', {"users" : users })

def roles_permission(request):
    roles_permission = [
        {
            "Role_Name": "Admin",
            "Created_On": "27 Mar 2024",
        },
        {
            "Role_Name": "Student",
            "Created_On": "20 Mar 2024",
        },
        {
            "Role_Name": "Parent",
            "Created_On": "16 Mar 2024",
        },
        {
            "Role_Name": "Guardian",
            "Created_On": "26 Feb 2024",
        },
        {
            "Role_Name": "Librarian",
            "Created_On": "15 Feb 2024",
        },
        {
            "Role_Name": "Accountant",
            "Created_On": "13 Feb 2024",
        },
        {
            "Role_Name": "Driver",
            "Created_On": "28 Jan 2024",
        },
        {
            "Role_Name": "Coach",
            "Created_On": "21 Jan 2024",
        },
        {
            "Role_Name": "Warden",
            "Created_On": "10 Jan 2024",
        },
        {
            "Role_Name": "Therapist",
            "Created_On": "24 Dec 2024",
        }
    ]
    return render(request, 'pages/user-management/roles-permission.html', {"roles_permission" : roles_permission})

def permission(request):
    permission = [
        {
            "Modules": "Classes"
        },
        {
            "Modules": "Class Routine"
        },
        {
            "Modules": "Sections"
        },
        {
            "Modules": "Subjects"
        },
        {
            "Modules": "Sylabus"
        },
        {
            "Modules": "Time Table"
        },
        {
            "Modules": "Home Work"
        },
        {
            "Modules": "Library"
        },
        {
            "Modules": "Sports"
        },
        {
            "Modules": "Transport"
        }
    ]
    return render(request, 'pages/user-management/permission.html', {"permission" : permission})

def delete_account(request):
    delete_account = [
        {
            "ID": "U461893",
            "Name": "Janet",
            "Image": "assets/img/students/student-01.jpg",
            "Requisition_Date": "25 Mar 2024",
            "Delete_Request_Date": "27 Mar 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461892",
            "Name": "Joann",
            "Image": "assets/img/students/student-02.jpg",
            "Requisition_Date": "18 Mar 2024",
            "Delete_Request_Date": "20 Mar 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461891",
            "Name": "Kathleen",
            "Image": "assets/img/students/student-03.jpg",
            "Requisition_Date": "14 Mar 2024",
            "Delete_Request_Date": "16 Mar 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461890",
            "Name": "Gifford",
            "Image": "assets/img/students/student-04.jpg",
            "Requisition_Date": "27 Feb 2024",
            "Delete_Request_Date": "26 Feb 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461889",
            "Name": "Lisa",
            "Image": "assets/img/students/student-05.jpg",
            "Requisition_Date": "13 Feb 2024",
            "Delete_Request_Date": "15 Feb 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461888",
            "Name": "Ralph",
            "Image": "assets/img/students/student-06.jpg",
            "Requisition_Date": "11 Feb 2024",
            "Delete_Request_Date": "13 Feb 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461887",
            "Name": "Julie",
            "Image": "assets/img/students/student-07.jpg",
            "Requisition_Date": "26 Jan 2024",
            "Delete_Request_Date": "28 Jan 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461886",
            "Name": "Ryan",
            "Image": "assets/img/students/student-08.jpg",
            "Requisition_Date": "19 Jan 2024",
            "Delete_Request_Date": "21 Jan 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461885",
            "Name": "Susan",
            "Image": "assets/img/students/student-09.jpg",
            "Requisition_Date": "08 Jan 2024",
            "Delete_Request_Date": "10 Jan 2024",
            "Status": "Confirm"
        },
        {
            "ID": "U461884",
            "Name": "Susan",
            "Image": "assets/img/students/student-10.jpg",
            "Requisition_Date": "22 Dec 2024",
            "Delete_Request_Date": "24 Dec 2024",
            "Status": "Confirm"
        }
    ]
    return render(request, 'pages/user-management/delete-account.html', {"delete_account" : delete_account})

    
# Membership

def membership_plans(request):
    return render(request, 'pages/membership/membership-plans.html')

def membership_addons(request):
    return render(request, 'pages/membership/membership-addons.html')

def membership_transactions(request):
    membership_transactions = [
        {
            "ID": "MT156328",
            "Provider_Name": "Green Valley High School",
            "Plan_Type": "Starter",
            "Transaction_Date": "25 Apr 2024",
            "Amount": "$99",
            "Payment_Method": "Cash",
            "Start_Date": "25 Apr 2024",
            "End_Date": "24 May 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156327",
            "Provider_Name": "Riverside Academy",
            "Plan_Type": "Enterprise",
            "Transaction_Date": "29 Apr 2024",
            "Amount": "$149",
            "Payment_Method": "Credit",
            "Start_Date": "29 Apr 2024",
            "End_Date": "28 May 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156326",
            "Provider_Name": "Sunshine School",
            "Plan_Type": "Starter",
            "Transaction_Date": "03 May 2024",
            "Amount": "$99",
            "Payment_Method": "Cash",
            "Start_Date": "03 May 2024",
            "End_Date": "02 Jun 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156325",
            "Provider_Name": "Maplewood High School",
            "Plan_Type": "Premium",
            "Transaction_Date": "15 May 2024",
            "Amount": "$199",
            "Payment_Method": "Cash",
            "Start_Date": "15 May 2024",
            "End_Date": "14 Jun 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156324",
            "Provider_Name": "Mountain High School",
            "Plan_Type": "Enterprise",
            "Transaction_Date": "15 May 2024",
            "Amount": "$149",
            "Payment_Method": "Cash",
            "Start_Date": "25 May 2024",
            "End_Date": "24 Jun 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156323",
            "Provider_Name": "Hillside Elementary School",
            "Plan_Type": "Starter",
            "Transaction_Date": "12 Jun 2024",
            "Amount": "$99",
            "Payment_Method": "Credit",
            "Start_Date": "12 Jun 2024",
            "End_Date": "11 Jul 2024",
            "Status": "Pending"
        },
        {
            "ID": "MT156322",
            "Provider_Name": "Willow Creek High School",
            "Plan_Type": "Starter",
            "Transaction_Date": "17 Jun 2024",
            "Amount": "$99",
            "Payment_Method": "Cash",
            "Start_Date": "17 Jun 2024",
            "End_Date": "16 Jul 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156321",
            "Provider_Name": "Brookside High School",
            "Plan_Type": "Premium",
            "Transaction_Date": "26 Jun 2024",
            "Amount": "$199",
            "Payment_Method": "Cash",
            "Start_Date": "26 Jun 2024",
            "End_Date": "25 Jul 2024",
            "Status": "Pending"
        },
        {
            "ID": "MT156320",
            "Provider_Name": "Cedar Grove Academy",
            "Plan_Type": "Enterprise",
            "Transaction_Date": "03 Jul 2024",
            "Amount": "$149",
            "Payment_Method": "Credit",
            "Start_Date": "03 Jul 2024",
            "End_Date": "02 Aug 2024",
            "Status": "Completed"
        },
        {
            "ID": "MT156319",
            "Provider_Name": "Westfield Elementary School",
            "Plan_Type": "Starter",
            "Transaction_Date": "12 Jul 2024",
            "Amount": "$99",
            "Payment_Method": "Cash",
            "Start_Date": "12 Jul 2024",
            "End_Date": "11 Aug 2024",
            "Status": "Completed"
        }
    ]
    return render(request, 'pages/membership/membership-transactions.html', {"membership_transactions" : membership_transactions})

    # Layout

def layout_default(request):
    return render(request, 'pages/layout/layout-default.html')

def layout_mini(request):
    return render(request, 'pages/layout/layout-mini.html')

def layout_rtl(request):
    return render(request, 'pages/layout/layout-rtl.html')

def layout_box(request):
    return render(request, 'pages/layout/layout-box.html')

def layout_dark(request):
    return render(request, 'pages/layout/layout-dark.html')

def under_maintenance(request):
    return render(request, 'pages/pages/under-maintenance.html')

def coming_soon(request):
    return render(request, 'pages/pages/coming-soon.html')


    # Pages

def profile(request):
    return render(request, 'pages/pages/profile.html')

def lock_screen(request):
    return render(request, 'pages/pages/lock-screen.html')

def blank_page(request):
    return render(request, 'pages/pages/blank-page.html')

def error_404(request):
    return render(request, 'pages/pages/404-error.html')

def error_500(request):
    return render(request, 'pages/pages/500-error.html')

def activites(request):
    return render(request, 'pages/activites.html')




