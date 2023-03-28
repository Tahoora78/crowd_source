from django.contrib.auth.models import User
from django.http import HttpResponse
import math

def update_scores(user):
    user.profile.score += 1
    user.profile.level = math.floor(math.sqrt(user.profile.score))
    user.profile.save()
