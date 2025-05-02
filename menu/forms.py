from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation

def validate_name_russian(value):
    import re
    if not re.fullmatch(r"[А-Яа-яЁё\s-]+", value):
        raise ValidationError('Имя должно содержать только русские буквы, пробелы и дефисы.')
                                                  
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'guests', 'time', 'agree']
        labels = {'name': 'Имя', 'phone': 'Телефон', 'guests': 'Количество гостей', 'time': 'Время бронирования', 'agree': 'Согласен с условиями бронирования'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'guests': forms.NumberInput(attrs={'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'agree': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

        error_messages = {
            'name': {
                'required': 'Пожалуйста, укажите ваше имя.',
                'max_length': 'Имя слишком длинное.',
            },
            'phone': {
                'required': 'Введите номер телефона.',
            },
            'guests': {
                'required': 'Укажите количество гостей.',
                'min_value': 'Минимум 1 гость.',
                'max_value': 'Максимум 20 гостей.',
            },
            'time': {
                'required': 'Укажите время.',
            },
            'agree': {
                'required': 'Необходимо согласиться с условиями.',
            },
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        validate_name_russian(name)  # твоя проверка на русский язык
        return name

    def clean_guests(self):
        guests = self.cleaned_data['guests']
        if not (1 <= guests <= 20):
            raise forms.ValidationError('Количество гостей должно быть от 1 до 20.')
        return guests



# class ReservationForm(forms.Form):
#     name = forms.CharField(
#         label="Ваше имя",
#         max_length=100,
#         validators=[validate_name_russian],
#         widget=forms.TextInput(attrs={'class': 'form-input'}),
#         error_messages={
#             'required': 'Пожалуйста, укажите ваше имя.',
#             'max_length': 'Имя слишком длинное.',
#         }
#     )
    
#     phone = forms.CharField(
#         label="Телефон",
#         max_length=20,
#         widget=forms.TextInput(attrs={'class': 'form-input'}),
#         error_messages={
#             'required': 'Введите номер телефона.',
#         }
#     )

#     guests = forms.IntegerField(
#         label="Количество гостей",
#         min_value=1,
#         max_value=20,
#         widget=forms.NumberInput(attrs={'class': 'form-input'}),
#         error_messages={
#             'required': 'Укажите количество гостей.',
#             'min_value': 'Минимум 1 гость.',
#             'max_value': 'Максимум 20 гостей.',
#         }
#     )

#     time = forms.TimeField(
#         label="Время бронирования",
#         widget=forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
#         error_messages={
#             'required': 'Укажите время.',
#         }
#     )

#     agree = forms.BooleanField(
#         label="Согласен с условиями бронирования",
#         required=True,
#         initial=True,
#         error_messages={
#             'required': 'Необходимо согласиться с условиями.'
#         }
#     )