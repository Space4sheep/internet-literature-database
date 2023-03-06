# Generated by Django 4.1.5 on 2023-02-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_book_bookshelf_book_bookshelf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='url',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=1, max_length=50, verbose_name='Жанр'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='url_book',
            field=models.CharField(max_length=200, null=True, verbose_name='Посилання на книгу'),
        ),
        migrations.AddField(
            model_name='book',
            name='url_image',
            field=models.CharField(max_length=250, null=True, verbose_name='Посилання на зображення'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='Автор'),
        ),
    ]
