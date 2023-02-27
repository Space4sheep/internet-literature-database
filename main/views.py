from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Bookshelf, Rating, Article
from .forms import BookshelfForm, BookForm, SelectBookshelfForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpRequest


def index(request):
    """Головна сторінка"""
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def article(request, article_id):
    """Сторінка кожної окремої статті"""
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article.html', {'article': article})


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


def book_page(request, book_id):
    """Функція, яка обробляє всі події на сторінці конкретної книги."""
    book = get_object_or_404(Book, pk=book_id)

    rating = Rating.objects.filter(book=book, user=request.user).first()
    book.user_rating = rating.rating if rating else 0

    if request.method == 'POST':
        if 'bookshelf' in request.POST:
            bookshelf_form = SelectBookshelfForm(request.POST, instance=book, user=request.user)
            if bookshelf_form.is_valid():
                bookshelf_id = bookshelf_form.cleaned_data['bookshelf'].values_list('id', flat=True).first()
                book = bookshelf_form.save(commit=False)
                book.save()
                bookshelf_form.save_m2m()
                return redirect('main:bookshelf', bookshelf_id=bookshelf_id)
            else:
                review_form = ReviewForm()
        elif 'text_review' in request.POST:
            bookshelf_form = SelectBookshelfForm(instance=book, user=request.user)
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                print(review_form)
                review = review_form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()
                return redirect('main:book', book_id=book.id)
        else:
            bookshelf_form = SelectBookshelfForm(instance=book, user=request.user)
            review_form = ReviewForm()
    else:
        bookshelf_form = SelectBookshelfForm(instance=book, user=request.user)
        review_form = ReviewForm()

    context = {
        'bookshelf_form': bookshelf_form,
        'book': book,
        'review_form': review_form
    }

    return render(request, 'main/book.html', context)


@login_required
def bookshelf(request, bookshelf_id):
    """Сторінка конкретної полиці"""
    bookshelf = Bookshelf.objects.get(id=bookshelf_id)
    books = bookshelf.book_set.order_by('-id')
    return render(request, 'main/bookshelf.html', {'bookshelf': bookshelf, 'books': books})


@login_required
def delete_bookshelf(request, bookshelf_id):
    """Видалити полицю"""
    bookshelf = Bookshelf.objects.get(pk=bookshelf_id)
    bookshelf.delete()
    return redirect('main:bookshelves')


@login_required
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
    bookshelves = Bookshelf.objects.filter(user=request.user).order_by('date_added')
    return render(request, 'main/bookshelves.html', {'bookshelves': bookshelves})


@login_required
def new_bookshelf(request):
    if request.method != 'POST':
        form = BookshelfForm()
    else:
        form = BookshelfForm(data=request.POST)
        if form.is_valid():
            new_bookshelf = form.save(commit=False)
            new_bookshelf.user = request.user
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

