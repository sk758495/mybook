from django.db import models

class Book(models.Model):
    author_name = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    publish_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_photo = models.ImageField(upload_to='book_covers/')
    logo = models.ImageField(upload_to='book_logos/')

    def __str__(self):
        return self.book_name
