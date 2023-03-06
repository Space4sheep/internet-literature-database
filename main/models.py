from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Bookshelf(models.Model):
    """Topics by which the user sorts books in his library."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Книжкова полиця'
        verbose_name_plural = 'Книжкові полиці'

    def __str__(self):
        return self.title


class Book(models.Model):
    """Модель книги"""
    bookshelf = models.ManyToManyField(Bookshelf, blank=True)
    title = models.CharField('Назва', max_length=100)
    author = models.CharField('Автор', max_length=100, null=True)
    description = models.TextField('Опис')
    genre = models.CharField('Жанр', max_length=50)
    url_book = models.CharField('Посилання на книгу', max_length=200, blank=True, null=True)
    url_image = models.CharField('Посилання на зображення', max_length=250, null=True)

    def average_rating(self) -> float:
        return Rating.objects.filter(book=self).aggregate(Avg("rating"))["rating__avg"] or 0

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.title}, {self.average_rating()}, {self.author}"


class Rating(models.Model):
    """Модель для додавання оцінок до книги"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.book.title}: {self.rating}"


class Review(models.Model):
    """Модель для створення рецензій до книг"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    text_review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_review


class ArticleCategory(models.Model):
    """Модель для створення категорій для сортування статей"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    """Модель для створення статей"""
    title = models.CharField('Заголовок', max_length=250)
    categories = models.ManyToManyField(ArticleCategory, related_name='articles')
    text = models.TextField("Текст статті")
    image = models.ImageField(upload_to='article_images/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='articles')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
