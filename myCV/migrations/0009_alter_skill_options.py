# Generated by Django 5.0.2 on 2024-03-20 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0008_alter_skill_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('-order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]