from django.shortcuts import render
from .models import Book


def index(request):
    """Main page of main"""
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})


def results(request):
    """Results page"""
    return render(request, 'main/results.html')


def about(request):
    """Сторінка про нас"""
    return render(request, 'main/about.html')


def library(request):
    """Вивід бібліотеки"""
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})
