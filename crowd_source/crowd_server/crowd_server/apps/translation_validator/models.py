from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    cert_text1 = models.CharField(max_length=200)
    cert_text2 = models.CharField(max_length=200)
    no_count = models.PositiveIntegerField(default=0)
    yes_count = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    not_sure_count = models.PositiveIntegerField(default=0)
    
    class FinalAnswer(models.IntegerChoices):
        NO = 0
        YES = 1
        NOT_ANSWERED = -1

    final_answer = models.IntegerField(choices=FinalAnswer.choices, default=-1)

    def __str__(self):
        return f'{self.id} - {self.question_text}'

    def save(self, *args, **kwargs):
        self.count = self.no_count + self.yes_count
        super().save(*args, **kwargs)


class QuestionUser(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='qu_translation_validator')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qu_translation_validator')
    
    class Answer(models.IntegerChoices):
        NO = 0
        YES = 1
        NOT_SURE = 2
        NOT_ANSWERED = -1

    answer = models.IntegerField(choices=Answer.choices, default=-1)

