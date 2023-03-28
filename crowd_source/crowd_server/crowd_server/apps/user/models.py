from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"score: {self.score} | level: {self.level}"
        