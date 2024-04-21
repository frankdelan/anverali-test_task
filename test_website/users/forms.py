from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=255)

    first_name = forms.CharField(label='Имя', max_length=255)

    last_name = forms.CharField(label='Фамилия', max_length=255)

    email = forms.EmailField(label='Электронная почта', max_length=255)

    is_customer = forms.ChoiceField(label='Статус', choices=((0, 'Исполнитель'),
                                                          (1, 'Заказчик')))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "is_customer")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=255)

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password")
