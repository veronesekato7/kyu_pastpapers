from django.contrib import admin
from .models import University, Department, Course, Year, CourseUnit, Paper

#Register your models here.
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(CourseUnit)
