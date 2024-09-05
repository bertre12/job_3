from django.shortcuts import render
from rest_framework import generics

from drf.serializer import StudentSerializer
from student.models import Student


class StudentList(generics.ListAPIView):  # Только чтение.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
