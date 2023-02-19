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
    bookshelf = forms.ModelMultipleChoiceField(
        queryset=Bookshelf.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select-lg col-5'}),
        label='',
        required=False
    )

    class Meta:
        model = Book
        fields = ['bookshelf']

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        super(SelectBookshelfForm, self).__init__(*args, **kwargs)
        self.fields['bookshelf'].queryset = Bookshelf.objects.filter(owner=owner)
        self.fields['bookshelf'].label_from_instance = lambda obj: obj.title

