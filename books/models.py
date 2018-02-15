from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, default='')
    author = models.CharField(max_length=100, blank=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], blank=True, null=True)

    class Meta:
        ordering = ('-rating', '-created')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.lower().replace(' ', '_')
        return super(Book, self).save(*args, **kwargs)


class Note(TimeStampedModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()
