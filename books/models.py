from django.db import models


# Create your models here.

class Book(models.Model):
    genre_options = (
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science fiction', 'Science Fiction'),
        ('thriller', 'Thriller'),
        ('non-fiction', 'Non-Fiction')
    )

    cover_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    genre = models.CharField(choices=genre_options, max_length=15)
    release_year = models.IntegerField()
    description = models.TextField(max_length=3000)

    def __str__(self):
        return f'{self.title}{self.author}'
