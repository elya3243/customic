from django.db import models
from django.contrib.auth.models import User


class Dress(models.Model):
    image = models.ImageField()
    mockup = models.ForeignKey('Mockup', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return str(self.id)


class Mockup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mockups', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text

