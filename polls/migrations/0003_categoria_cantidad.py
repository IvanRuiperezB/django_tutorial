# Generated by Django 4.2 on 2024-12-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='Cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
