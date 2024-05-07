from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.subject}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = "Сообщения"
