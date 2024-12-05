from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
