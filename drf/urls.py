from django.urls import path
from .views import StudentList

urlpatterns = [
    path('list/', StudentList.as_view()),  # Отображение всех студентов.
]
