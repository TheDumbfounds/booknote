from django import forms
from .models import Book, Note


class CustomNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')
