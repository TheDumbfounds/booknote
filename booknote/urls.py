from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('', include('books.urls')),
    path('admin/', admin.site.urls),
]
