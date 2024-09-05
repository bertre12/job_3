from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.hashers import check_password


# Вход пользователя.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            try:
                # Проверка пользователя по имени.
                student = Student.objects.get(name=name)

                # Проверка пароля.
                if check_password(password, student.password):
                    # Перенаправление после успешного входа.
                    return redirect('home')
                else:
                    form.add_error(None, 'Неверные учетные данные.')

            except Student.DoesNotExist:
                form.add_error(None, 'Пользователь не найден.')

    else:
        form = LoginForm()

    return render(request, 'student/login.html', {'form': form})


# Страница приветствия после успешного входа.
def home(request):
    return HttpResponse('<h1> Вход на сайт <h1>')


# Регистрация нового пользователя.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            level = form.cleaned_data['level']

            # Создание нового пользователя.
            student = Student(name=name)
            # Хешируем пароль.
            student.set_password(password)
            # Устанавливаем/выбираем уровень доступа.
            student.level = level
            # Сохранение пользователя в бд.
            student.save()

            # Перенаправление на страницу входа.
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'student/register.html', {'form': form})


