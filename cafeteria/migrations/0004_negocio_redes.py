# Generated by Django 3.2.12 on 2023-02-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0003_negocio'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='redes',
            field=models.ManyToManyField(to='cafeteria.RedSocial'),
        ),
    ]