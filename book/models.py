from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

now = timezone.now()


class MyRestaurantUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', blank=True, max_length=50)

    # allows to pop up on the page and it will list the name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Branch(models.Model):
    name = models.CharField('Branch Name', max_length=120)
    address = models.CharField(max_length=300)
    branch_email = models.EmailField('Branch Email', max_length=50)
    branch_phone = models.CharField('Branch Phone', max_length=50)

    # allows to pop up on the page and it will list the name

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Guest Name', max_length=50)
    phone = models.CharField('Guest Phone', max_length=50)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
    book_date = models.DateField(default=datetime.now)
    book_time = models.TimeField(default=datetime.now)
    people = models.CharField('# of Guest', max_length=3)
    message = models.TextField(blank=True)
    myrestaurantuser = models.ForeignKey(MyRestaurantUser, blank=True,
                                         null=True, on_delete=models.CASCADE)

    # allows to pop up on the page and it will list the name
    def __str__(self):
        return self.name
