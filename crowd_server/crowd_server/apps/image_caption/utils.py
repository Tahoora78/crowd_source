from urllib import request
from .models import Question_User, Question
import math
from django.db.models import Max
from django.db.models import Q


def update_user_score(question):
    question_users_answered = Question_User.objects.filter(question=question)
    for question_user in question_users_answered:
        if question.final_answer==question_user.answer:
            question_user.user.profile.score += 1
            question_user.user.profile.level = math.floor(math.sqrt(question_user.user.profile.score)) 
            question_user.user.profile.save()
            question_user.user.save()


def get_question(request):
    user = request.user
    answered_questions = [question.id for question in Question_User.objects.filter(user=user)]
    #question = Question.objects.filter(count__lte=10)
    question = list(question.exclude(Q(id__in = answered_questions) | Q(count__gt=10)).order_by('-count')[0].values())
    return question