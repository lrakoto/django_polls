from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import Question


# Create your views here.
#def index(request):
    #return render(request, 'index.html')

def index(request):
    questions = list(Question.objects.all())
    return render(request, 'index.html', { 'questions': questions })

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        message = 'Question does not exist'
        return render(request, '404.html', { 'message': message })
    return render(request, 'detail.html', { 'question': question })

def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'results.html', { 'question': question })

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'vote.html', { 'question': question })

def polls(request):
    questions = list(Question.objects.all())
    return render(request, 'polls/index.html', { 'questions': questions})