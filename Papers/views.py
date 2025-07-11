from django.shortcuts import render, redirect
from .forms import UniversityForm, DepartmentForm, CourseForm, YearForm, CourseUnitForm, PaperForm
from .models import University, Department, Course, Year, CourseUnit, Paper

# Home Page
def home(request):
    return render(request, 'home.html')

# Add and list universities
def university_list_create(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_list')
    else:
        form = UniversityForm()
    
    universities = University.objects.all()
    return render(request, 'university_list.html', {'form': form, 'universities': universities})
