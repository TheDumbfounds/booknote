from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('books/add/', views.BookAddView.as_view(), name='book-add'),
    path('books/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/', views.BookListView.as_view(), name='booklist'),
]
