from django import forms
from .models import Level, Student


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


# Форма отображения изменяемых данных.
class EditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['password', 'nickname_tg', 'nickname_inst', 'status']
