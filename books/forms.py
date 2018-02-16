from django import forms
from .models import Book, Note


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CustomNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')
