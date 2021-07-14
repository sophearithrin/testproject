from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    return render(request, 'polls/index.html', {'questions': questions, 'choices': choices})
