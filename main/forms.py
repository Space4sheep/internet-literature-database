from django import forms

from .models import Bookshelf, Book, Review, Feedback


class BookshelfForm(forms.ModelForm):
    """Форма для створення полиці"""
    class Meta:
        model = Bookshelf
        fields = ['title']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['theme', 'text']


class BookForm(forms.ModelForm):
    """Форма для додавання книги до БД"""
    class Meta:
        model = Book
        fields = ['title', 'author']


class SelectBookshelfForm(forms.ModelForm):
    """Додає книгу на конкретну полицю"""
    bookshelf = forms.ModelMultipleChoiceField(
        queryset=Bookshelf.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select-lg col-12'}),
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
    """Форма для додавання рецензій"""
    class Meta:
        model = Review
        fields = ['text_review']
        labels = {
            'text_review': ''
        }
        widgets = {
            'text_review': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 40,
                                                 'placeholder': 'Ви можете написати тут свою рецензію на цю книгу'})
        }
