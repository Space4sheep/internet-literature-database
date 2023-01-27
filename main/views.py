from django.shortcuts import render


def index(request):
    """Main page of main"""
    return render(request, 'main/index.html')
