from statistics import mode
from time import sleep
from django.db import models
from django.contrib.auth.models import User
from . import constants



class Question(models.Model):
    image_link1 = models.CharField(max_length=800)
    image_link2 = models.CharField(max_length=800)
    question_text = models.CharField(max_length=100)
    photo1_count = models.IntegerField(default=0)
    photo2_count = models.IntegerField(default=0)
    similar_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    
    class FinalAnswer(models.IntegerChoices):
        PHOTO1 = 0
        PHOTO2 = 1
        SIMILAR = 2
        NOT_DEFINED = -1

    final_answer = models.IntegerField(choices=FinalAnswer.choices, default=-1)

    def save(self, *args, **kwargs):
        self.count = self.photo1_count + self.photo2_count + self.similar_count
        counts_list = [self.photo1_count, self.photo2_count, self.similar_count]
        if self.count>=constants.THRESHOLD and counts_list.count(max(counts_list))==1:
            max_count = max(counts_list)
            self.final_answer = counts_list.index(max_count)
        super(Question, self).save(*args, **kwargs)


class QuestionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qu_food_compare')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField()

        