from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class AskQuestionPage(CreateView):
    template_name = 'collaborate/askQuestion.html'
    form_class = AskQuestionForm
    success_url = reverse_lazy('home')

def SaveQuestion(request):
    form = AskQuestionForm()

    if request.method == 'POST':
        form = AskQuestionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
    return render(request,'collaborate/success.html',{'form':form})

def AnswerQuestionPage(request,id):

    qns = AskQuestion.objects.get(questionid=id)
    ans = QuestionAnswer.objects.filter(questionid=id).order_by('-timestamp')
    form = QuestionAnswerForm
   
    return render(request,'collaborate/answerQuestion.html',{'qns':qns,'form':form,'ans':ans})

def SaveAnswer(request,id):
    form = QuestionAnswerForm()
    

    if request.method == 'POST':
        form = QuestionAnswerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return redirect(request.META['HTTP_REFERER'])
