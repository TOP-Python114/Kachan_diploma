from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Введите жанр книги",
        verbose_name="Жанр книги"
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите язык книги",
        verbose_name="Язык книги"
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя автора"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия автора"
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        null=True,
        blank=True
    )
    date_of_death = models.DateField(
        verbose_name="Дата смерти",
        null=True,
        blank=True
    )
    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/',
        verbose_name="Картинка",

    )

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название книги"
    )
    genre = models.ForeignKey(
        'Genre', on_delete=models.CASCADE,
        verbose_name="Жанр книги",
        null=True
    )
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE,
        verbose_name="Язык книги",
        null=True
    )
    author = models.ManyToManyField(
        'Author',
        verbose_name="Автор книги",
    )
    summary = models.TextField(
        max_length=1000,
        verbose_name="Аннотация книги",
    )
    isn = models.CharField(
        max_length=13,
        verbose_name="ISBN книги",
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='files/',
        verbose_name="Файл",

    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/',
        verbose_name="Картинка",

    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'

