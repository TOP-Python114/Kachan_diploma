from django import forms
from datetime import date
from .models import Book, Genre, Language, Author
from django.forms import ModelForm


class AuthorForm(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    date_of_birth = forms.DateField(label='Дата рождения',
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type':'date'}))
    date_of_death = forms.DateField(label='Дата смерти',
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    foto_author = forms.ImageField(label='Фото')


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isn', 'file', 'image']








