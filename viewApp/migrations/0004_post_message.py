# Generated by Django 2.1.2 on 2018-11-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewApp', '0003_auto_20181118_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
    ]
