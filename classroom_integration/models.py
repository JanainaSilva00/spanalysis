from django.db import models
from teacher.models import Teacher


class Credentials(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete="CASCADE")
    client_id = models.CharField(max_length=150)
    api_key = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150, blank=True)
