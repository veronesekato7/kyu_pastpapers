from django.shortcuts import render, redirect

from .models import University, Department, Course, Year, CourseUnit, Paper

# Home Page
def home(request):
    return render(request, 'home.html')
