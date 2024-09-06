from django.urls import path
from .views import StudentList, CreateStudentView

urlpatterns = [
    path('list/', StudentList.as_view()),  # Отображение списка всех студентов.
    path('create_student/', CreateStudentView.as_view()),  # Регистрация
    # нового студента.
]
