# Generated by Django 5.0.2 on 2024-03-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0014_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the settings', max_length=255, verbose_name='name')),
                ('button_text', models.CharField(blank=True, default='', max_length=255, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]
