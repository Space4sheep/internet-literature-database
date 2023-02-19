from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Bookshelf, Rating
from .forms import BookshelfForm, BookForm, SelectBookshelfForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpRequest


def index(request):
    """Головна сторінка"""
    return render(request, 'main/index.html')


def library(request):
    """Вивід всіх книг"""
    books = Book.objects.all()
    return render(request, 'main/library.html', {'books': books})


def about(request):
    """Сторінка про нас"""
    return render(request, 'main/about.html')


def rate(request: HttpRequest, book_id: int, rating: int) -> HttpResponse:
    book = Book.objects.get(id=book_id)
    Rating.objects.filter(book=book, user=request.user).delete()
    book.rating_set.create(user=request.user, rating=rating)
    return index(request)


def add_book_to_bookshelf(request, book_id):
    """Додавання конктретної книги на конкретну полицю"""
    book = get_object_or_404(Book, pk=book_id)
    if request.method != 'POST':
        form = SelectBookshelfForm(instance=book, owner=request.user)
    else:
        form = SelectBookshelfForm(request.POST, instance=book, owner=request.user)

        if form.is_valid():

            book = form.save(commit=False)
            book.save()
            form.save_m2m()

            return redirect('main:bookshelves')
    return render(request, 'main/book.html', {'form': form, 'book': book})


@login_required
def bookshelf(request, bookshelf_id):
    """Сторінка конкретної полиці"""
    bookshelf = Bookshelf.objects.get(id=bookshelf_id)
    books = bookshelf.book_set.order_by('-id')
    return render(request, 'main/bookshelf.html', {'bookshelf': bookshelf, 'books': books})


def delete_bookshelf(request, bookshelf_id):
    """Видалити полицю"""
    bookshelf = Bookshelf.objects.get(pk=bookshelf_id)
    bookshelf.delete()
    return redirect('main:bookshelves')


def delete_book_from_bookshelf(request, book_id, bookshelf_id):
    """Прибрати книгу з полиці"""
    book = Book.objects.get(pk=book_id)
    bookshelf = Bookshelf.objects.get(pk=bookshelf_id)
    book.bookshelf.remove(bookshelf)
    return redirect('main:bookshelf', bookshelf_id)


@login_required
def bookshelves(request):
    """Вивід всії полиць"""
    # Відображаємо лише полиці власника і сортуємо за датою
    bookshelves = Bookshelf.objects.filter(owner=request.user).order_by('date_added')
    return render(request, 'main/bookshelves.html', {'bookshelves': bookshelves})


def new_bookshelf(request):
    if request.method != 'POST':
        form = BookshelfForm()
    else:
        form = BookshelfForm(data=request.POST)
        if form.is_valid():
            new_bookshelf = form.save(commit=False)
            new_bookshelf.owner = request.user
            new_bookshelf.save()
            return redirect('main:bookshelves')
    return render(request, 'main/new_bookshelf.html', {'form': form})


def add_book(request, bookshelf_id):
    """Переробити для додавання рецензій"""
    bookshelf = Bookshelf.objects.get(id=bookshelf_id)
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.bookshelf = bookshelf
            new_book.save()
            return redirect('main:bookshelf', bookshelf_id=bookshelf_id)
    return render(request, 'main/add_book.html', {"bookshelf": bookshelf, 'form': form})


def search_books(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return render(request, 'main/search_books.html', {})
    else:
        searched = request.POST['searched']
        books = Book.objects.filter(Q(author__iregex=searched) | Q(title__iregex=searched))
        for book in books:
            rating = Rating.objects.filter(book=book, user=request.user).first()
            book.user_rating = rating.rating if rating else 0
        return render(request, 'main/search_books.html', {'searched': searched, 'books': books})



