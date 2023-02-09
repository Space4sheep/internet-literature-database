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


class SelectBookshelfForm(forms.Form):
    select_bookshelf = forms.ModelChoiceField(queryset=Bookshelf.objects.all(), label='Полиця')


