# Generated by Django 3.2.18 on 2023-02-26 14:22

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0029_alter_book_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_time',
            field=models.TimeField(default=book.models.get_current_time),
        ),
    ]
