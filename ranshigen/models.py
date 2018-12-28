from django.db import models
from django.utils import timezone

class Generator(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    definition = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    res_id = models.CharField(max_length=128)

    def __str__(self):
        return self.name
