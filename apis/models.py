from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Image(models.Model):
    title = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title