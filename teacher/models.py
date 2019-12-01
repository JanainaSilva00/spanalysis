from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    university_cod = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.firstname