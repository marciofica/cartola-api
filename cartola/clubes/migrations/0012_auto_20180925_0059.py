# Generated by Django 2.1 on 2018-09-25 00:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubes', '0011_auto_20180924_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogadorclube',
            name='clube',
        ),
        migrations.AddField(
            model_name='jogadorclube',
            name='clube',
            field=models.ManyToManyField(to='clubes.Clube'),
        ),
        migrations.RemoveField(
            model_name='jogadorclube',
            name='usuario',
        ),
        migrations.AddField(
            model_name='jogadorclube',
            name='usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
