from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'Latest_question_list': latest_question_list}
    return render(request, 'eventos/index.html', context)

def details(request, question_id):
    return HttpResponse('Essa é a pergunta de número %s' %question_id)

def results(request, question_id):
    return HttpResponse('Esses são os resultados da pergunta número %s' %question_id)

def vote(request, question_id):
    return HttpResponse('Você está votando na pergunta número %s' %question_id)
