from django.urls import path

from . import views

app_name = 'marks_system'

# Matched by order be carefull !
urlpatterns = [
    # **Courses**

    # ex: /marks_system/ all courses
    path('courses/', views.IndexView.as_view(), name='index'),

    #ex: /marks_system/students view used in order to add a student
    # path('courses/<str:code>/edit', views.CourseUpdate.as_view(), name='course-update'),
    path('courses/<str:code>/edit', views.update_course, name='course-update'),

    # ex: /marks_system/1/ given course
    path('courses/<str:code>/', views.course_detail, name='detail'),

    # **Student**
    # ex: /marks_system/students/1/ a given student
    path('students/<int:pk>/edit', views.update_student, name='update-student'),

    # **Student**
    # ex: /marks_system/students/1/ a given student
    path('students/<int:pk>/', views.DetailStudentView.as_view(), name='detail-student'),

    # forms
    #ex: /marks_system/students view used in order to add a student
    path('students/', views.get_students, name='students'),


]