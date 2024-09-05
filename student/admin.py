from django.contrib import admin

from student.models import Student

# Регистрация таблицы.
admin.site.register(Student)
