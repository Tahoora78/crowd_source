from statistics import mode
from time import sleep
from django.db import models
from django.contrib.auth.models import User
from . import constatnts



class Question(models.Model):
    image_link = models.CharField(max_length=800)
    question_text = models.CharField(max_length=100)
    cert_text = models.CharField(max_length=100)
    no_count = models.IntegerField(default=0)
    yes_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    not_sure_count = models.IntegerField(default=0)
    
    class FinalAnswer(models.IntegerChoices):
        NO = 0
        YES = 1
        NOT_ANSWERED = -1

    final_answer = models.IntegerField(choices=FinalAnswer.choices, default=-1)

    def save(self, *args, **kwargs):
        self.count = self.yes_count + self.no_count
        if self.count>=constatnts.THRESHOLD:
            self.final_answer = 1 if self.yes_count>self.no_count else 1
        super(Question, self).save(*args, **kwargs)


class Question_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qu_image_caption')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField()

        