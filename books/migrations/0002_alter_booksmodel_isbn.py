# Generated by Django 5.0.6 on 2024-06-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
