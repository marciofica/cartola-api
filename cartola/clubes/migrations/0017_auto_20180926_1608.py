# Generated by Django 2.1 on 2018-09-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubes', '0016_partida_clube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='clube',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubes.Clube'),
        ),
    ]
