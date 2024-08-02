from django.db import models

# Create your models here.

class Either(models.Model):
    title = models.CharField(max_length=100)
    a = models.TextField()
    b = models.TextField()

class Comment(models.Model):
    A = 'A'
    B = 'B'
    Choice = [
        (A, 'A'),
        (B, 'B'),
    ]

    content = models.TextField()
    choice = models.CharField(max_length=100, choices=Choice)
    either = models.ForeignKey(Either, on_delete=models.CASCADE)