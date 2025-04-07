from django.shortcuts import render

# Create your views here.

# Main

def index(request):
    return render(request, 'pages/dashboard/index_6pbs.html')

def teacher_dashboard(request):
    teachers = [
        {
            "id": "35013",
            "name": "Janet",
            "image": "assets/img/students/student-01.jpg",
            "class": "III",
            "section": "A",
            "marks": "89%",
            "cgpa": "4.2",
            "status": "Pass"
        },
        {
            "id": "35013",
            "name": "Joann",
            "image": "assets/img/students/student-02.jpg",
            "class": "IV",
            "section": "B",
            "marks": "88%",
            "cgpa": "3.2",
            "status": "Pass"
        },
        {
            "id": "35011",
            "name": "Kathleen",
            "image": "assets/img/students/student-03.jpg",
            "class": "II",
            "section": "A",
            "marks": "69%",
            "cgpa": "4.5",
            "status": "Pass"
        },
        {
            "id": "35010",
            "name": "Gifford",
            "image": "assets/img/students/student-04.jpg",
            "class": "I",
            "section": "B",
            "marks": "21%",
            "cgpa": "4.5",
            "status": "Pass"
        },
        {
            "id": "35009",
            "name": "Lisa",
            "image": "assets/img/students/student-05.jpg",
            "class": "II",
            "section": "B",
            "marks": "31%",
            "cgpa": "3.9",
            "status": "Fail"
        }
    ]
    return render(request, 'pages/dashboard/teacher-dashboard.html', {'teachers': teachers})

def student_dashboard(request):
    return render(request, 'pages/dashboard/student-dashboard.html')

def parent_dashboard(request):
    return render(request, 'pages/dashboard/parent-dashboard.html')