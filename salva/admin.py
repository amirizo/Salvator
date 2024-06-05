from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(QuestionCategory)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_type']
admin.site.register(Question, QuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display =['id', 'question', 'user', 'right_answer']

admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)

