from django import forms
from .models import Level


# Форма отображения при входе пользователя.
class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


# Форма отображения при регистрации нового пользователя.
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    level = forms.ModelChoiceField(queryset=Level.objects.all(),
                                   label='Уровень')
