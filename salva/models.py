from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class QuestionCategory(models.Model):
    title = models.CharField(max_length=224)
    detail = models.CharField(max_length=224)


    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title

    

class Question(models.Model):

    """ question model """

    QUESTION_TYPES = (
        ('MC', 'Multiple Choice'),
        ('FB', 'Fill in the Blank'),
    )
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=244)
    opt_1 = models.CharField(max_length=224)
    opt_2 = models.CharField(max_length=224)
    opt_3 = models.CharField(max_length=224)
    opt_4 = models.CharField(max_length=224)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)

    right_opt = models.CharField(max_length=224)


    class Meta:
        verbose_name_plural = "Question"

    def __str__(self):
        return self.question




class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'User Submitted Answers'
    


    

class Exercise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title