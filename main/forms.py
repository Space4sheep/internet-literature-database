from django import forms

from .models import Bookshelf, Book, Review


class BookshelfForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['title']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class SelectBookshelfForm(forms.ModelForm):
    """Додає книгу на конкретну полицю"""
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
        user = kwargs.pop('user')
        super(SelectBookshelfForm, self).__init__(*args, **kwargs)
        # Беремо тільки ті елементи "Bookshelf", власниками яких є поточний користувач
        self.fields['bookshelf'].queryset = Bookshelf.objects.filter(user=user)
        self.fields['bookshelf'].label_from_instance = lambda obj: obj.title


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text_review']
