from django.urls import path
from .views import StudentList, CreateStudentView, UpdateStudentView

urlpatterns = [
    path('list/', StudentList.as_view()),  # Отображение списка всех студентов.
    path('create_student/', CreateStudentView.as_view()),  # Регистрация
    # нового студента.
    path('update_student/<int:pk>/', UpdateStudentView.as_view(),
         name='update-student')  # Изменение данных студента.
]
