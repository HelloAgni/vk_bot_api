from django.db import models


class City(models.Model):
    """Название города"""
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
