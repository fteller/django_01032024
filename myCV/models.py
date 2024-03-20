from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class AbstractModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="created_date", help_text="")
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name="updated_date", help_text="")

    class Meta:
        abstract = True

# Create your models here.
class GeneralSetting(AbstractModel):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name="name", help_text="This is variable of the settings")
    description = models.CharField(max_length=255, default='', blank=True, verbose_name="description", help_text="")
    parameter = models.CharField(max_length=255, default='', blank=True, verbose_name="parameter", help_text="")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="created_date", help_text="")
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name="updated_date", help_text="")


    def __str__(self):
        return f'General Setting: {self.name}'


    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractModel):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name="name", help_text="This is variable of the settings")
    description = models.CharField(max_length=255, default='', blank=True, verbose_name="description", help_text="")
    file = models.ImageField(default='', blank=True, verbose_name="Image", help_text="", upload_to='images/')

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(default=0, verbose_name="order", help_text="")
    name = models.CharField(max_length=255, default='', blank=True, verbose_name="name", help_text="")
    percentage = models.IntegerField(default=0, blank=True, verbose_name="percentage", validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)

class Experience(AbstractModel):
    company_name = models.CharField(max_length=255, default='', verbose_name="Company Name", blank=True, help_text="")
    job_title = models.CharField(max_length=255, default='', verbose_name="Job Title", blank=True, help_text="")
    job_location = models.CharField(max_length=255, default='', verbose_name="Job Location", blank=True, help_text="")
    start_date = models.DateField(verbose_name="Start Date", help_text="")
    end_date = models.DateField(default=None, verbose_name="End Date", null=True, blank=True, help_text="")

    def __str__(self):
        return f'Experience: {self.company_name} - {self.job_title}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)