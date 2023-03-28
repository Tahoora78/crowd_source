from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from crowd_server.apps.food_fact.models import Question, QuestionUser
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from django.http import JsonResponse
from django.http import  HttpRequest
from . import constants
import math
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import FoodFactSerializer


NO = constants.NO
YES = constants.YES
NOT_SURE = constants.NOT_SURE
SCORE_THRESHOLD = constants.SCORE_THRESHOLD



class FoodFact(CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodFactSerializer

    def post(self, requset: HttpRequest, format = None):
        try:
            question_id = int(requset.POST.get('question_id'))
            answer = int(requset.POST.get('label'))
            question = Question.objects.get(id = question_id)
            user = requset.user
            QuestionUser.objects.create(question = question, answer = answer, user = user)

            if answer == YES:
                question.yes_count += 1
                question.count += 1
            elif answer == NO:
                question.no_count += 1
                question.count += 1
            elif answer == NOT_SURE:
                question.not_sure_count += 1
            
            question.save()
            if question.count >= SCORE_THRESHOLD:
                question.final_answer = YES if question.yes_count > question.no_count else NO
                question.save()

                rewarded_users = QuestionUser.objects.filter(question = question, answer = question.final_answer)
                rewarded_users = [qs.user for qs in rewarded_users]

                for user in rewarded_users:
                    user.profile.score += 1
                    user.profile.level = math.floor(math.sqrt(user.profile.score))
                    user.profile.save()
                    user.save()
            
            response_data = {}
            response = JsonResponse(response_data, status=201)
            return response

        except Exception as e:
            response_data = {"status": "failed", "message": e}
            response = JsonResponse(response_data, status = 400)
            return response
    

    def get(self, request: HttpRequest):
        user = request.user
        answered_questions = [qs.question.id for qs in QuestionUser.objects.filter(user=user)]
        questions = Question.objects.exclude(Q(id__in=answered_questions) | Q(count__gte=SCORE_THRESHOLD)).order_by('-count')
        question = questions[0]

        image_link = question.image_link
        question_text = question.question_text   
        question_id = question.id

        response_data = {"image_link": image_link, "question_text": question_text, "question_id": question_id}
        response = JsonResponse(response_data)
        return response     
