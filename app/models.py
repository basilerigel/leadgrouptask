from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.TextField(max_length=200, null=True)
    age = models.IntegerField()


class Drink(models.Model):
    name = models.TextField(max_length=250)


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pair = models.BooleanField(default=False)
    drink = models.ForeignKey(Drink, on_delete=models.SET_NULL, null=True)
