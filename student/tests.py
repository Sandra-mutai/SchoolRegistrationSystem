from _typeshed import Self
from django.test import TestCase
from .models import Student
from django.urls import reverse
import datetime


# Create your tests here.
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="jane",
            last_name="doe",
            age=20
        )

def test_full_name_contains_first_name(self):
    self.assertIn(self.student.first_name, self.student.fullname())

def test_full_name_contains_last_name(self):
    self.assertIn(self.student.last_name, self.student.fullname())


def test_year_of_birth(self):
    year=datetime.datetime.now().year-self.student.age
    self.assertEqual(year,self.student.year_of_birth())

def test_student_registration_view(self):
    self.data={"first_name": self.student.first_name,
               "last_name":self.student.last_name,
               "age":self.student.age  }

    url=reverse("register_student")
    response=self.Client.post(url,self.data)
    self.assertEqual(response.status_code,200)