# Generated by Django 2.1 on 2018-10-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0017_auto_20180926_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidaconfirmacao',
            name='confirmado',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='partidaconfirmacao',
            name='dh_confirmacao',
            field=models.DateTimeField(null=True),
        ),
    ]