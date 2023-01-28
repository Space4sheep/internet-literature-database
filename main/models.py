from django.db import models


class Bookshelf(models.Model):
    """Topics by which the user sorts books in his library."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Bookshelves'

    def __str__(self):
        return self.title


class Book(models.Model):
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.author}"

