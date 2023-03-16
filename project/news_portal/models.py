import datetime

from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum

class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    post = models.ForeignKey(
        to='Post',
        on_delete=models.CASCADE,
        related_name='news',
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name.title()}: {self.description[:30]}'


class Post(models.Model):
    name = models.CharField(max_length=100, unique=True)



    def __str__(self):
        return self.name.title()


