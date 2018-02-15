from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/add-book.html'
    success_url = '/books'
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    fields = '__all__'
    success_url = '/books'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
