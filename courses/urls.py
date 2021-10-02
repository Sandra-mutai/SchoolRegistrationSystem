from django.urls import path
from .views import register_courses, courses_list

urlpatterns=[
    path("register/", register_courses,name="register_courses"),
    path("list/", courses_list,name="courses_list"),


]
