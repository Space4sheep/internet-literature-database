from django.shortcuts import render, redirect
from .models import Book, Bookshelf
from .forms import BookshelfForm, BookForm, SelectBookshelfForm
from django.contrib.auth.decorators import login_required


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


def book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = SelectBookshelfForm()
    else:
        form = SelectBookshelfForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'main/book.html', {'form': form, 'book': book})


@login_required
def bookshelf(request, bookshelf_id):
    bookshelf = Bookshelf.objects.get(id=bookshelf_id)
    books = bookshelf.book_set.order_by('-date_added')
    return render(request, 'main/bookshelf.html', {'bookshelf': bookshelf, 'books': books})


@login_required
def bookshelves(request):
    """Вивід всії полиць"""
    bookshelves = Bookshelf.objects.order_by('date_added')
    return render(request, 'main/bookshelves.html', {'bookshelves': bookshelves})


def new_bookshelf(request):
    if request.method != 'POST':
        form = BookshelfForm()
    else:
        form = BookshelfForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelves')
    return render(request, 'main/new_bookshelf.html', {'form': form})


def add_book(request, bookshelf_id):
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



