from django.db import models


class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    subtitle = models.CharField(max_length=100)
    pages = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
