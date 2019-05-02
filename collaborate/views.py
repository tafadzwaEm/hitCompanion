from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,DetailView,TemplateView
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
    context = {
        'qns':qns,
        'form':form,
        'ans':ans,
       
    }
   
    return render(request,'collaborate/answerQuestion.html',context)

def SaveAnswer(request,id):
    form = QuestionAnswerForm()
    

    if request.method == 'POST':
        form = QuestionAnswerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return redirect(request.META['HTTP_REFERER'])

def like_post(request):
    an = get_object_or_404(QuestionAnswer,answerid=request.POST.get('answerid'))
    an.likes.add(request.user)
    return redirect(request.META['HTTP_REFERER'])

class FeedbackPage(CreateView):
    template_name = "collaborate/feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy('home')

class ContactPage(TemplateView):
    template_name = "collaborate/contact.html"
    
