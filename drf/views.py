from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from drf.serializer import StudentSerializer, StudentUpdateSerializer
from student.models import Student


# Отображение пользователей.
class StudentList(generics.ListAPIView):  # Только чтение.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Создание нового пользователя для всех.
class CreateStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        # Проверка на существование пользователя с таким же именем.
        if Student.objects.filter(
                name=serializer.validated_data['name']).exists():
            raise ValidationError(
                {"name": "Пользователь с таким именем уже существует."})

        # Получаем данные.
        student = serializer.save()
        # Хэширование пароля.
        student.password = make_password(student.password)
        student.save()


# Изменение данных.
class UpdateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    lookup_field = 'pk'
