from django.shortcuts import render
from .models import Question, QuestionUser
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView 
from . import constants
from .utils import update_scores 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from .serializers import TranslationValidatorSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TranslationValidatorView(CreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Question.objects.all()
    serializer_class = TranslationValidatorSerializer

    def get(self, request):
        user = request.user
        answered_questions = [x.question.id for x in QuestionUser.objects.filter(user=user)]
        questions = Question.objects.exclude(Q(id__in=answered_questions) | Q(count__gte=constants.SCORE_THRESHOLD)).order_by('-count')
        question = questions[0]

        response_data = {'question_text': question.question_text, 'cert_text1': question.cert_text1,
                         'cert_text2': question.cert_text2, 'question_id': question.id}

        response = JsonResponse(response_data, status=200)
        return response
        

    def post(self, request, format=None):
        try:
            question_id = int(request.POST.get('question_id'))
            answer = int(request.POST.get('label'))
            question = Question.objects.get(pk=question_id)
            user = request.user
            QuestionUser.objects.create(question=question, user=user, answer=answer)
 
            if answer == constants.NO:
                question.no_count += 1
            elif answer == constants.YES:
                question.yes_count += 1
            elif answer == constants.NOT_SURE:
                question.not_sure_count += 1

            question.save()

            if question.count >= constants.SCORE_THRESHOLD:
                question.final_answer = constants.YES if question.yes_count > question.no_count else constants.NO
                awarded_question_users = QuestionUser.objects.filter(question=question, answer=question.final_answer)
                awarded_users = set(question_user.user for question_user in awarded_question_users)
                for user in awarded_users:
                    update_scores(user)

            question.save()

            response_data = {}
            response = JsonResponse(response_data, status=201)
            return response


        except:
            response_data = {'status': 'failed', 'message': 'Something went wrong'}
            response = JsonResponse(response_data, status=400)
            return response

