# Generated by Django 5.0.6 on 2024-06-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_booksmodel_author_alter_booksmodel_in_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='in_stock',
            field=models.IntegerField(),
        ),
    ]
