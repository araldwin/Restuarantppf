# Generated by Django 3.2.17 on 2023-02-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_auto_20230222_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='people',
            field=models.CharField(max_length=2, verbose_name='# of Guest'),
        ),
    ]
