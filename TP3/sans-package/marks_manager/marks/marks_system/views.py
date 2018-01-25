from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Examination, Student, Course, Mark
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import CreateStudentForm, CourseForm, StudentUpdateForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'marks_system/index.html'

    def get_queryset(self):
        """Return courses."""
        return Course.objects.all()
'''
class CourseUpdate(generic.UpdateView):
    model = Course
    fields = ['code', 'subject', 'start_date', 'end_date']
    exclude = []
    template_name = 'marks_system/update_course.html'
    success_url = '/marks_system/'
'''

def update_course(request, code):
    obj = get_object_or_404(Course, code=code)
    form = CourseForm(request.POST or None,
                        request.FILES or None, instance=obj)
    if request.method == 'POST':
        print(form)
        if form.is_valid():
           form.save()
           print("course UPDATED")
           return HttpResponseRedirect('/marks-system/courses')

    return render(request, 'marks_system/update_course.html', {'form': form})

# Hack for custom call, can be improved
def course_detail(request, code):
    course = get_object_or_404(Course, code=code)
    return render(request, 'marks_system/course_detail.html', {'course': course})

class DetailStudentView(generic.DetailView):
    model = Student
    template_name = 'marks_system/student_detail.html'

# On sort du canevas = code infecte
def get_students(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateStudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newStudent = Student(last_name=request.POST.get("last_name"), first_name=request.POST.get("first_name"), birth_date=request.POST.get("birth_date"))
            newStudent.save()

            print("***Student : "+str(newStudent.last_name) + " " + str(newStudent.first_name) + " saved-***")

            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        students = Student.objects.all()
        form = CreateStudentForm()

    return render(request, 'marks_system/students.html', {'form': form, 'students': students})

class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = ['last_name', 'first_name']
    template_name = 'marks_system/update_student.html'

def update_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    form = StudentUpdateForm(request.POST or None,
                        request.FILES or None, instance=obj)
    if request.method == 'POST':
        print(form)
        if form.is_valid():
           form.save()
           print("student UPDATED")
           return HttpResponseRedirect('/marks-system/students')

    return render(request, 'marks_system/update_student.html', {'form': form})
