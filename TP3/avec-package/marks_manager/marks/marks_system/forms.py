from django import forms

from .models import Course

class CreateStudentForm(forms.Form):
    last_name = forms.CharField(label='Last Name', max_length=200)
    first_name = forms.CharField(label='First Name', max_length=200)
    birth_date = forms.DateTimeField(label='Birth Date')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ['code', 'subject', 'start_date', 'end_date']
        fields = ['code', 'subject']
