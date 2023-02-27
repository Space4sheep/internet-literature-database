from django.contrib import admin

from .models import Bookshelf, Book, Article, ArticleCategory


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title__icontains', 'author__icontains']


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories', 'books',)
    search_fields = ['title', 'text', 'books__title', 'books__author__username']


admin.site.register(Book, BookAdmin)
admin.site.register(Bookshelf)
admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)

