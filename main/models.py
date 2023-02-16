from django.db import models


class Bookshelf(models.Model):
    """Topics by which the user sorts books in his library."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Книжкова полиця'
        verbose_name_plural = 'Книжкові полиці'

    def __str__(self):
        return self.title


class Book(models.Model):
    bookshelf = models.ManyToManyField(Bookshelf)
    title = models.CharField('Назва', max_length=100)
    author = models.CharField('Автор', max_length=100, null=True)
    genre = models.CharField('Жанр', max_length=50)
    url_book = models.CharField('Посилання на книгу', max_length=200, null=True)
    url_image = models.CharField('Посилання на зображення', max_length=250, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.title}, {self.author}"
