from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # print("sssssssssssssssssssssssssssssssssssssssssssssssssssss")
    return render(request, 'eventos/index.html', context)

#  def details(request, question_id):
    # return HttpResponse('Essa é a pergunta de número %s' %question_id)

# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'eventos/detail.html', {'question': question})

def results(request, question_id):
    # question = Question(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    # print(f"Question: {question}")
    # print(f"Question text: {question.question_text}")
    # print(f"Choices: {question.choice_set.all()}")
    return render(request, 'eventos/results.html', {'question': question })
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'eventos/vote.html', {
            'question': question,
            'error_message': "Você não escolheu uma opção",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('eventos:results', args=(question.id,)))




    # return HttpResponse('Você está votando na pergunta número %s' %question_id)
