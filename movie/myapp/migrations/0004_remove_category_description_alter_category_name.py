# Generated by Django 5.0.3 on 2024-03-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category_movie_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
