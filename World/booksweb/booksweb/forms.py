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

#
# class BookForm(forms.Form):
#     title = forms.CharField(label='Название книги')
#     genre = forms.MultipleChoiceField(
#         choices=[(p.id, p.name) for p in Genre.objects.all()],
#         label="Жанр книги"
#     )
#     language = forms.MultipleChoiceField(
#         choices=[(p.id, p.name) for p in Language.objects.all()],
#         label="Язык книги"
#     )
#     author = forms.MultipleChoiceField(
#         choices=[(p.id, p.last_name) for p in Author.objects.all()],
#         label="Автор книги")
#     summary = forms.CharField(label="Аннотация книги")
#     isn = forms.CharField(label="ISBN книги")
#     file = forms.FileField(label="Файл")


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language','author', 'summary', 'isn','file']




