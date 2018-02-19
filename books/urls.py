from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', include([
        path('modal/<int:note_id>', views.render_modal, name='modal'),
        path('modal/', views.render_modal, name='modal'),
        path('', views.BookListView.as_view(), name='list'),
        path('new', views.BookCreateView.as_view(), name='add'),
        path('<slug:slug>', include([
            path('delete', views.BookDeleteView.as_view(), name='delete'),
            path('', views.BookDetailView.as_view(), name='detail'),
        ])),
    ])),
]
