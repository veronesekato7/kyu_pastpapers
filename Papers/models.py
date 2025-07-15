from django.db import models

# Create your models here.
#University name top
class University(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
 #Department under university second   
class Department(models.Model):
    name = models.ForeignKey(University,on_delete = models.CASCADE,related_name='departments')
    #def __str__(self):
   #     return f"{self.name} ({self.university.name})"
    
    def get_university(self, obj):
        # Example: if Department has related Course, and Course has University
        return obj.course.university.name if obj.course and obj.course.university else 'N/A'
    get_university.short_description = 'University'
    




#Course under university third    
class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete = models.CASCADE,related_name='courses')
    def __str__(self):
        return f"{self.name} - {self.department.name}"

#Year under course fourth
class Year(models.Model):
    year_number = models.PositiveSmallIntegerField()  # e.g., 1 for Year 1, 2 for Year 2
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='years')

    def __str__(self):
        return f"Year {self.year_number} - {self.course.name}"


#course unit under year
class CourseUnit(models.Model):
    name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='course_units')

    def __str__(self):
        return f"{self.name} - {self.year}"

#paper under course unit with upload in pdf
class Paper(models.Model):
    title = models.CharField(max_length=200)
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE, related_name='papers')
    file = models.FileField(upload_to='papers/')  # optional: attach PDF or document
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.course_unit}"