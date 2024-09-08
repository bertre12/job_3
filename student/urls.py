from django.urls import path

from .views import login_view, register_view, private_view, edit_view, \
    logout_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Страница входа.
    path('logout/', logout_view, name='logout'),  # Путь для выхода.
    path('register/', register_view, name='register'),  # Страница регистрации.
    path('private/', private_view, name='private'),  # Страница пользователя.
    path('edit/', edit_view, name='edit'),  # Для изменения данных.
]
