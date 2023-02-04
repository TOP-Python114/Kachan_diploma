from django import forms
from datetime import date


class AuthorForm(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    date_of_birth = forms.DateField(label='Дата рождения',
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type':'date'}))
    date_of_death = forms.DateField(label='Дата смерти',
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class BookForm(forms.Form):
    title = forms.CharField(label='Название книги')
    genre = forms.CharField(label="Жанр книги")
    language = forms.CharField(label="Язык книги")
    author = forms.CharField(label="Автор книги")
    summary = forms.CharField(label="Аннотация книги")
    isn = forms.CharField(label="ISBN книги")
    file = forms.FileField(label="Файл")




