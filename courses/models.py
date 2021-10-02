from django.db import models


class Courses(models.Model):
    course_name=models.CharField(max_length=10)
    course_code=models.CharField(max_length=4)
    course_trainer =models.CharField(max_length=15)
    course_duration =models.DateField()
    course_material =models.FileField()
    syllabus=models.FileField()
    description=models.TextField()



