# Generated by Django 2.1.2 on 2018-11-18 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewApp', '0007_auto_20181118_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
    ]
