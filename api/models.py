from django.db import models

class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=80)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Fullname: {self.fullname} - Nickname: {self.nickname} - Age: {self.age} - Active: {self.is_active}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name: {self.name} - Amount: {self.amount}"
