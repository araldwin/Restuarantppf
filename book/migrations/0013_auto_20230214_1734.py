# Generated by Django 3.2.17 on 2023-02-14 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.RemoveField(
            model_name='book',
            name='guest',
        ),
        migrations.AddField(
            model_name='book',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.myrestaurantuser'),
        ),
    ]
