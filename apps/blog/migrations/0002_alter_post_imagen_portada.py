# Generated by Django 4.0.1 on 2022-01-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen_portada',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Imagen de Portada'),
        ),
    ]
