# Generated by Django 4.1.5 on 2023-02-11 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksweb', '0004_alter_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Дата смерти'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='booksweb.author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booksweb.genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isn',
            field=models.CharField(max_length=13, verbose_name='ISBN книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booksweb.language', verbose_name='Язык книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=1000, verbose_name='Аннотация книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
    ]
