from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import LoginForm, RegistrationForm, EditForm
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
                    # Сохраняем данные о пользователе в сессии.
                    request.session['student_id'] = student.id
                    # Перенаправление после успешного входа.
                    return redirect('private')
                else:
                    form.add_error(None, 'Неверные учетные данные.')

            except Student.DoesNotExist:
                form.add_error(None, 'Пользователь не найден.')

    else:
        form = LoginForm()

    return render(request, 'student/login.html', {'form': form})


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


# Отображение данных студента после входа.
def private_view(request):
    # Получаем id студента из сессии.
    student_id = request.session.get('student_id')
    # Получаем информацию о студенте
    student = get_object_or_404(Student, id=student_id)

    return render(request, 'student/private.html', {'student': student})


# Изменение данных студента.
def edit_view(request):
    # Получаем id студента из сессии.
    student_id = request.session.get('student_id')
    # Получаем информацию о студенте.
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=student)
        if form.is_valid():
            # Сохранение изменений.
            form.save()
            # Перенаправление на личный кабинет после сохранения.
            return redirect('private')
    else:
        form = EditForm(instance=student)

    return render(request, 'student/edit.html', {'form': form})


# Выход пользователя.
def logout_view(request):
    if 'student_id' in request.session:
        # Удаляем id студента из сессии.
        del request.session['student_id']
    # Перенаправляем на страницу входа.
    return redirect('login')
