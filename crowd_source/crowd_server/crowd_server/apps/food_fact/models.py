from random import choices
from django.db import models
from django.contrib.auth.models import User
from . import constants

NO = constants.NO
YES = constants.YES
NOT_SURE = constants.NOT_SURE


class Question(models.Model):
    image_link = models.CharField(max_length=1000)
    question_text = models.CharField(max_length=100000)
    no_count = models.IntegerField(default=0)
    yes_count = models.IntegerField(default=0)
    not_sure_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    
    class FinalAnswer(models.IntegerChoices):
        NO = 0
        YES = 1
        NOT_ANSWERED = -1

    final_answer = models.IntegerField(choices=FinalAnswer.choices, default=-1)

    def __str__(self):
        return self.question_text
    

class QuestionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qu_food_fact')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    class Answer(models.IntegerChoices):
        NO = 0
        YES = 1
        NOT_ANSWERED = -1
    
    answer = models.IntegerField(choices=Answer.choices, default=-1)






