from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('bookshelves/', views.bookshelves, name='bookshelves'),
    path('bookshelf/<int:bookshelf_id>/', views.bookshelf, name='bookshelf'),
    path('rate/<int:book_id>/<int:rating>/', views.rate),
    path('new_bookshelf/', views.new_bookshelf, name='new_bookshelf'),
    path('book/<int:book_id>/', views.book_page, name='book'),
    path('delete_bookshelf/<int:bookshelf_id>/', views.delete_bookshelf, name='delete_bookshelf'),
    path('delete_book_from_bookshelf/<int:book_id>/<int:bookshelf_id>/', views.delete_book_from_bookshelf,
         name='delete_book_from_bookshelf'),
    path('search_books/', views.search_books, name='search_books')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


