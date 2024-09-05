from django.urls import path
from .views import login_view, register_view, home

urlpatterns = [
    path('login/', login_view, name='login'),  # Страница входа.
    path('register/', register_view, name='register'),  # Страница регистрации.
    path('home/', home, name='home'),  # Переход на домашнюю страницу.
]