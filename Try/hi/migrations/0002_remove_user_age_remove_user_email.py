# Generated by Django 4.1.7 on 2023-08-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
