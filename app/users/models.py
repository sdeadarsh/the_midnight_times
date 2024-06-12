from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    quota = models.PositiveBigIntegerField(default=15)
    is_active = models.BooleanField(default=True)
    last_time_stamp = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)