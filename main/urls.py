from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('library/', views.library, name='library'),
    path('bookshelves/', views.bookshelves, name='bookshelves'),
    path('bookshelf/<int:bookshelf_id>/', views.bookshelf, name='bookshelf'),
    path('new_bookshelf/', views.new_bookshelf, name='new_bookshelf'),
    path('add_book/<int:bookshelf_id>/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book, name='book')
]
