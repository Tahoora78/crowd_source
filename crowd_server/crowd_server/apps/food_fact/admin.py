from django.contrib import admin
from .models import Question
from .models import QuestionUser

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','image_link', 'question_text', 'no_count', 'yes_count', 'not_sure_count', 'count', 'final_answer']

class QuestionUserAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'question', 'answer']

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionUser,QuestionUserAdmin)

