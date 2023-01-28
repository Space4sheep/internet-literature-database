from django.shortcuts import render


def index(request):
    """Main page of main"""
    return render(request, 'main/index.html')


def results(request):
    """Results page"""
    return render(request, 'main/results.html')


def about(request):
    """Сторінка про нас"""
    return render(request, 'main/about.html')
