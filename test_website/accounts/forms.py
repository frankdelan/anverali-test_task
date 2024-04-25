from django import forms
from django.contrib.auth import get_user_model
from django.forms import FileInput

from users.choices import EXPERIENCE_TYPES

User = get_user_model()


class EditExecutorForm(forms.ModelForm):
    about = forms.CharField(label='О себе', max_length=1000, widget=forms.Textarea(attrs={'rows': 4}))

    experience = forms.ChoiceField(label='Опыт работы', choices=EXPERIENCE_TYPES)

    telegram = forms.CharField(label='Telegram', widget=forms.TextInput(attrs={'placeholder': "@example"}))

    photo = forms.ImageField(label='Фотография', required=False, widget=FileInput)

    class Meta:
        model = User
        fields = ['photo', 'about', 'experience', 'telegram']


class EditCustomerForm(forms.ModelForm):
    telegram = forms.CharField(label='Telegram', widget=forms.TextInput(attrs={'placeholder': "@example"}))

    photo = forms.ImageField(label='Фотография', required=False, widget=FileInput)

    class Meta:
        model = User
        fields = ['photo', 'telegram']