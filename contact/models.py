from django.db import models
from myCV.models import AbstractModel


# Create your models here.

class Message(AbstractModel):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name="Name", help_text="")
    email = models.EmailField(max_length=255, default='', blank=True, verbose_name="Email",
                              help_text=" ")
    subject = models.CharField(max_length=255, default='', blank=True, verbose_name="Subject", help_text="")
    message = models.TextField(default='', blank=True, verbose_name="Message", help_text="")

    def __str__(self):
        return f'Message: {self.name} - {self.email}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('name',)
