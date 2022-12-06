from django.http import HttpResponse
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
    return render(request, 'detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def polls(request):
    questions = list(Question.objects.all())
    return render(request, 'polls/index.html', { 'questions': questions})