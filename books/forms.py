from django import forms
from .models import Book, Note


class CustomNoteForm(forms.ModelForm):
    note_id = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Note
        fields = ('title', 'body')
