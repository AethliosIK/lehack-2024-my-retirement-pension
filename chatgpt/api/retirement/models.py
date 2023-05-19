from django.db import models

class Retirement(models.Model):
    uuid = models.UUIDField(primary_key=True)
    retirement = models.IntegerField(default=64)
