# Generated by Django 3.2.18 on 2023-02-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0027_alter_book_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='people',
            field=models.IntegerField(verbose_name='Number of Guest'),
        ),
    ]
