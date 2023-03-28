from django.contrib import admin
from .models import Question, QuestionUser


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'id', 'yes_count', 'no_count', 'not_sure_count', 'final_answer',)
    list_filter = ('yes_count', 'no_count')


class QuestionUserAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer')


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionUser, QuestionUserAdmin)
