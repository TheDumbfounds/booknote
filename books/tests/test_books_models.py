import pytest
from mixer.backend.django import mixer
from books.models import Book
pytestmark = pytest.mark.django_db


class TestBook:
    def test_model(self):
        obj = mixer.blend('books.Book', name='Two Scoops Of DJANGO')
        assert obj.pk == 1, 'Should save a book instance'
        assert obj.slug == 'two_scoops_of_django', 'Should assign slug after save'


class TestNote:
    def test_model(self):
        obj = mixer.blend('books.Note')
        assert obj.pk == 1, 'Should save a note instance'
