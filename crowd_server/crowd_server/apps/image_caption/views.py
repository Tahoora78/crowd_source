from telnetlib import STATUS
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Question_User, Question
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import update_user_score, get_question
from . import constatnts
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.http import JsonResponse
from django.db.models import Q
from .serializers import ImageCaptionSerializer


class ImageCaption(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageCaptionSerializer

    def post(self, request, format=None):
        try:
            if request.user.is_authenticated:
                answer = int(request.POST['label'])
                question = Question.objects.get(id=request.POST['question_id'])
                #user = User.objects.get(username=request.user.username)
                user = request.user

                if answer == constatnts.YES:
                    question.yes_count += 1
                elif answer == constatnts.NO:
                    question.no_count += 1
                else:
                    question.not_sure_count += 1
                question.save()

                question_user = Question_User(question=question, user=user, answer=answer)                
                question_user.save()
                update_user_score(question)
                return JsonResponse({}, status=200)
        except Exception as e:
            response = {"status": "failed", "message": str(e)}
            return JsonResponse(response, status=400)
    
    
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            answered_questions = [question.question.id for question in Question_User.objects.filter(user=user)]
            question = Question.objects.exclude(Q(id__in = answered_questions) | Q(count__gt=constatnts.THRESHOLD)).order_by('-count')[0]
            response = {
                "image_link": question.image_link,
                "question_text": question.question_text,
                "cert_text": question.cert_text,
                "question_id": question.id
            }
            return JsonResponse(response, safe=False)
