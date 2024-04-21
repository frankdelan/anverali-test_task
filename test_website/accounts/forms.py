from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditExecutorForm(forms.ModelForm):
    about = forms.CharField(label='О себе', max_length=1000, widget=forms.Textarea(attrs={'rows': 4}))

    experience = forms.ChoiceField(label='Опыт работы', choices=(('Нет опыта', 'Нет опыта'),
                                                                 ('Несколько месяцев', 'Несколько месяцев'),
                                                                 ('От 1 до 3 лет', 'От 1 до 3 лет'),
                                                                 ('От 3 до 5 лет', 'От 3 до 5 лет'),
                                                                 ('Более 5 лет', 'Более 5 лет')))

    telegram = forms.CharField(label='Telegram', widget=forms.TextInput(attrs={'placeholder': "@example"}))

    class Meta:
        model = User
        fields = ['about', 'experience', 'telegram']


class EditCustomerForm(forms.ModelForm):
    telegram = forms.CharField(label='Telegram', widget=forms.TextInput(attrs={'placeholder': "@example"}))

    class Meta:
        model = User
        fields = ['telegram']