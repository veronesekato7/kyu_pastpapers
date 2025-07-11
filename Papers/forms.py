from django import forms
from .models import University, Department, Course, Year, CourseUnit, Paper

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'

class CourseUnitForm(forms.ModelForm):
    class Meta:
        model = CourseUnit
        fields = '__all__'

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'
