# Generated by Django 3.2.17 on 2023-02-17 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0015_alter_myrestaurantuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='myrestaurantuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='book',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Guest Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Guest Phone'),
        ),
    ]
