# Generated by Django 5.0.3 on 2024-03-18 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_category_movie_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
