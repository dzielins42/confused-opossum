from django.db import models
from django.utils import timezone

class Generator(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    definition = models.TextField(default='')
    res_id = models.CharField(max_length=128)

    def __str__(self):
        return self.name
