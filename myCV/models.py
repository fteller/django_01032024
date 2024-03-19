from django.db import models


# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name="name", help_text="This is variable of te settings")
    description = models.CharField(max_length=255, default='', blank=True, verbose_name="description", help_text="")
    parameter = models.CharField(max_length=255, default='', blank=True, verbose_name="parameter", help_text="")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="created_date", help_text="")
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name="updated_date", help_text="")


def __str__(self):
    return f'General Setting: {self.name}'


class Meta:
    verbose_name = 'General Setting'
    verbose_name_plural = 'General Settings'
    ordering = ('name')
