from django.shortcuts import render


def index(request):
    """Main page of ildb"""
    return render(request, 'ildb/index.html')
