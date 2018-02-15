import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from books.views import BookListView
from accounts import views
pytestmark = pytest.mark.django_db


class TestLoginView:
    def test_profile_anonymous(self):
        req = RequestFactory().get(reverse('profile'))
        req.user = AnonymousUser()
        resp = views.profile(req)
        assert resp.status_code == 302, 'Should redirect anonymous user to login page'

    def test_profile_authenticated(self):
        req = RequestFactory().get(reverse('profile'))
        req.user = mixer.blend(User)
        resp = views.profile(req)
        assert resp.status_code == 200, 'Should only be callable by anonymous users'
