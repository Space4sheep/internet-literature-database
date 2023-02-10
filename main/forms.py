from django import forms

from .models import Bookshelf, Book


class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['title']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class SelectBookshelfForm(forms.ModelForm):
    class Meta:
        model = Book

        #bookshelf = Bookshelf.objects.all()
        #select_bookshelf = forms.CharField(widget=forms.Select(choices=bookshelf))
        fields = ['bookshelf']
        #select_bookshelf = forms.ModelChoiceField(queryset=Bookshelf.objects.all(), label='Полиця')


