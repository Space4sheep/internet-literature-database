from django.contrib import admin

from .models import Bookshelf, Book

admin.site.register(Book)
admin.site.register(Bookshelf)
