# Generated by Django 5.0.3 on 2024-03-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_category_description_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
