import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from books.views import BookListView, BookDetailView
pytestmark = pytest.mark.django_db


class TestBookListView:
    def test_access_anonymous(self):
        req = RequestFactory().get(reverse('booklist'))
        req.user = AnonymousUser()
        resp = BookListView.as_view()(req)
        assert 'login' in resp.url, 'Should redirect to login page'

    def test_access_authenticated(self):
        req = RequestFactory().get(reverse('booklist'))
        req.user = mixer.blend(User)
        resp = BookListView.as_view()(req)
        assert resp.status_code == 200, 'Should display booklist'


class TestBookDetailView:
    def test_access(self):
        mixer.blend('books.Book', name='Two Scoops Of DJANGO')
        req = RequestFactory().get('/books/two_scoops_of_django')
        req.user = mixer.blend(User)
        resp = BookDetailView.as_view()(req)
        assert resp.status_code == 200, 'Should display detail view'
