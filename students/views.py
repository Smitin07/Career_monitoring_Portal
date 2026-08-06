from django.shortcuts import render, redirect
from .models import StudentProfile
from .forms import StudentForm


def home(request):
    return render(request, 'students/home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # ⭐ FILES added
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


def students_list(request):
    query = request.GET.get('q')

    students = StudentProfile.objects.all()

    if query:
        students = students.filter(skills__name__icontains=query).distinct()

    return render(request, 'students/list.html', {'students': students})


def profile(request, id):
    student = StudentProfile.objects.get(id=id)
    return render(request, 'students/profile.html', {'student': student})


def top_students(request):
    students = StudentProfile.objects.order_by('-cgpa')[:5]
    return render(request, 'students/top.html', {'students': students})


def shortlisted_students(request):
    students = StudentProfile.objects.filter(cgpa__gte=7)
    return render(request, 'students/shortlist.html', {'students': students})


def filter_students(request):
    cgpa = request.GET.get('cgpa')
    skill = request.GET.get('skill')

    students = StudentProfile.objects.all()

    if cgpa:
        students = students.filter(cgpa__gte=cgpa)

    if skill:
        students = students.filter(skills__name__icontains=skill).distinct()

    return render(request, 'students/filter.html', {'students': students})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'students/companies.html', {'companies': companies})
def company_detail(request, id):
    company = Company.objects.get(id=id)
    students = StudentProfile.objects.all()

    shortlisted = []

    for student in students:
        if student.cgpa >= company.min_cgpa:
            student_skills = student.skills.lower()
            company_skills = company.required_skills.lower()

            if any(skill in student_skills for skill in company_skills.split(',')):
                shortlisted.append(student)

    # sort by CGPA
    shortlisted = sorted(shortlisted, key=lambda x: x.cgpa, reverse=True)

    top_students = shortlisted[:10]

    return render(request, 'students/company_detail.html', {
        'company': company,
        'students': shortlisted,
        'top_students': top_students
    })