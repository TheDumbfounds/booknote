import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from books.views import BookListView, BookDetailView, BookDeleteView, BookCreateView
from ..models import Book
import json
pytestmark = pytest.mark.django_db


class TestBookListView:
    def test_access_anonymous(self):
        req = RequestFactory().get(reverse('books:list'))
        req.user = AnonymousUser()
        resp = BookListView.as_view()(req)
        assert 'login' in resp.url, 'Should redirect to login page'

    def test_access_authenticated(self):
        req = RequestFactory().get(reverse('books:list'))
        req.user = mixer.blend(User)
        resp = BookListView.as_view()(req)
        assert resp.status_code == 200, 'Should display booklist'


class TestBookDetailView:
    def test_access(self):
        book = mixer.blend('books.Book', name='Two Scoops Of DJANGO')
        req = RequestFactory().get('/books/two_scoops_of_django')
        req.user = mixer.blend(User)
        resp = BookDetailView.as_view()(req, slug=book.slug)
        assert resp.status_code == 200, 'Should display detail view'


class TestBookCreateView:
    def test_add(self):
        data = {
            'name': 'the test book'
        }
        req = RequestFactory().post('/books/new', data=data)
        req.user = mixer.blend(User)
        resp = BookCreateView.as_view()(req)

        assert Book.objects.filter(name='the test book').exists() == True
        assert resp.status_code == 302


class TestBookDeleteView:
    def test_delete(self):
        book = mixer.blend('books.Book', name='Two Scoops Of DJANGO')
        req = RequestFactory().post('/books/two_scoops_of_django/delete')
        req.user = mixer.blend(User)
        resp = BookDeleteView.as_view()(req, slug=book.slug)

        assert Book.objects.filter(slug=book.slug).exists() == False
        assert resp.url + '/' == reverse('books:list'), 'Should have deleted the book'
