from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, QueryDict
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Book, Note
from .forms import CustomNoteForm
import json


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

    def post(self, request, *args, **kwargs):
        form = CustomNoteForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, slug=kwargs['slug'])
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']

            Note.objects.create(
                title=title,
                body=body,
                author=request.user,
                book=book,
            ).save()

        return redirect(reverse('books:detail', kwargs={'slug': kwargs['slug']}))

    def delete(self, request, *args, **kwargs):
        note_id = QueryDict(request.body).get('note_id')
        note = get_object_or_404(Note, author=request.user, id=note_id)
        note.delete()
        return HttpResponse('')

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = CustomNoteForm()
        book = get_object_or_404(Book, slug=self.kwargs['slug'])
        context['notes'] = Note.objects.filter(book=book)
        return context


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/add-book.html'
    success_url = '/books'
    fields = ('name', 'author', 'rating')


@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    fields = '__all__'
    success_url = '/books'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
