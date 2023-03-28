from django.contrib import admin
from .models import Question
from .models import QuestionUser

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','image_link1','image_link2' ,'question_text', 'similar_count', 'photo2_count', 'photo1_count', 'count', 'final_answer']

class QuestionUserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'question', 'answer']

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionUser,QuestionUserAdmin)

