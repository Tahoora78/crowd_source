from telnetlib import STATUS
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import QuestionUser, Question
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import update_user_score
from . import constants
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.http import JsonResponse
from django.db.models import Q
from .serializers import FoodCompareSerializer


class FoodCompare(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodCompareSerializer 

    def post(self, request, format=None):
        try:
            if request.user.is_authenticated:
                answer = int(request.POST['label'])
                question = Question.objects.get(id=request.POST['question_id'])
                user = request.user

                if answer == constants.PHOTO1:
                    question.photo1_count += 1
                elif answer == constants.PHOTO2:
                    question.photo2_count += 1
                else:
                    question.similar += 1
                question.save()

                question_user = QuestionUser(question=question, user=user, answer=answer)                
                question_user.save()
                update_user_score(question)
                return JsonResponse({}, status=200)
        except Exception as e:
            response = {"status": "failed", "message": str(e)}
            return JsonResponse(response, status=400)
    
    
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            answered_questions = [question.question.id for question in QuestionUser.objects.filter(user=user)]
            question = Question.objects.exclude(Q(id__in = answered_questions) | ~Q(final_answer = -1)).order_by('-count')[0]
            response = {
                "image_link1": question.image_link1,
                "image_link2": question.image_link2,
                "question_text": question.question_text,
                "question_id": question.id
            }
            return JsonResponse(response, safe=False)
