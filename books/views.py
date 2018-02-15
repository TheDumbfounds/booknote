from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Book


@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'books/booklist.html'
    context_object_name = 'books'


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/bookdetail.html'
    context_object_name = 'book'
    slug_url_kwarg = 'slug'


@method_decorator(login_required, name='dispatch')
class BookAddView(CreateView):
    model = Book
    template_name = 'books/add-book.html'
    success_url = '/books'
    fields = '__all__'
