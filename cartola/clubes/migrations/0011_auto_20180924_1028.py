# Generated by Django 2.1 on 2018-09-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0010_auto_20180924_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='data_inscricao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='jogadorclube',
            name='data_membro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
