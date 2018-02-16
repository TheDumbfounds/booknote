from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('books/new', views.BookCreateView.as_view(), name='add'),
    path('books/<slug:slug>/', include([
        path('delete', views.BookDeleteView.as_view(), name='delete'),
        path('', views.BookDetailView.as_view(), name='detail'),
    ])),
    path('books/', views.BookListView.as_view(), name='list'),
]
