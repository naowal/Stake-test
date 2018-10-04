from django.db import models

from django.utils import timezone

class Message(models.Model):
    mid = models.AutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.text
