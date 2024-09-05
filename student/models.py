from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Таблица уровней доступа.
class Level(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', null=True)

    def __str__(self):
        return self.name

    # Для удобного отображения в админпанели.
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


# Талица для заполнения данных студента.
class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    image = models.ImageField(upload_to='static/images/', blank=True,
                              verbose_name='Фото')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    phone = models.CharField(max_length=255, verbose_name='№ телефона')
    email = models.EmailField(max_length=255,
                              verbose_name='Электронная почта')
    nickname_tg = models.CharField(max_length=255, blank=True,
                                   verbose_name='Никнейм Telegram')
    nickname_inst = models.CharField(max_length=255, blank=True,
                                     verbose_name='Никнейм Instagram')
    group_number = models.CharField(max_length=255, verbose_name='№ группы')
    balance = models.IntegerField(default=0,
                                  verbose_name='Количество баллов')
    status = models.CharField(max_length=100, verbose_name='Статус')
    service = models.CharField(max_length=255, verbose_name='Пакет услуг')
    internship = models.CharField(max_length=255, verbose_name='Стажировка')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True,
                              null=True, verbose_name='Уровень доступа')

    # Хеширование пароля при создании нового пользователя.
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

    # Для удобного отображения в админпанели.
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
