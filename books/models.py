from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, default='')
    author = models.CharField(max_length=100, blank=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], blank=True, null=True)

    def str(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(' ', '_')
        return super(Book, self).save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
