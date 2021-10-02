
import datetime
from django.db import models


class Student(models.Model):
    first_name=models.CharField(max_length=20,help_text="e.g. Sandra")
    last_name=models.CharField(max_length=16)
    age=models.PositiveSmallIntegerField()
    email=models.EmailField(max_length=30)
    # phone_number=models.CharField(max_length=15)
    student_id=models.CharField(max_length=12)
    student_class=models.CharField(max_length=10,null=True,blank=True)
    parent_name=models.CharField(max_length=14)
    parent_phone=models.CharField(max_length=13)
    passport=models.CharField(max_length=15,null=True,blank=True)
    mentor=models.CharField(max_length=10,null=True)
    room_number=models.CharField(max_length=3,null=True,blank=True)
    laptop_number=models.CharField(max_length=10,null=True,blank=True)
    big_sister =models.CharField(max_length=15,null=True)
    nationality=models.CharField(max_length=10,null=True)
    image=models.ImageField(null=True)
    COUNTRY_CHOICES=(
        (u'Kenya','Kenya'),
        (u'Uganda','Uganda'),
        (u'Rwanda','Rwanda')
    )
    country=models.CharField(max_length=8,choices=COUNTRY_CHOICES)

    NATIONALITY_CHOICES=(
     ("Kenyan","Kenyan"),
     ("Rwandese","Rwandese"),
     ("Ugandan","Ugandan"),
     ("Sudanese","Sudanese"),
     ("South Sudanese","South Sudanese"),
     ("Somalia","Somalia"),
    )
    nationality=models.CharField(max_length=15,choices=NATIONALITY_CHOICES,null=True)

    GENDER_CHOICES=(
        (u'Male','Male'),
        (u'Female','Female'),
        (u'Others','Others')
    )
    gender=models.CharField(max_length=8,choices=GENDER_CHOICES,null=True)

    def __str__(self):
        return self.first_name


    #  software testing

def full_name(self):
    return f"{self.first_name} {self.last_name}"
def year_of_birth(self):
    year=datetime.datetime.now().year-self.student.age
