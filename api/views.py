from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from student.models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
