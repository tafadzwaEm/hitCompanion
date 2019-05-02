from django.conf.urls import url 
from .views import *
from django.urls import path

app_name = 'collaborate'

urlpatterns = [
    url('askquestion',AskQuestionPage.as_view(),name='askQuestion'),
    url('saveQuestion/',SaveQuestion),
    path('comment/<int:id>/',AnswerQuestionPage),
    path('saveAnswer/<int:id>/',SaveAnswer),
    url('like/',like_post,name='like_post'),
    url('feedback/',FeedbackPage.as_view(),name="feedback"),
    url('contact/',ContactPage.as_view(),name="contact")
]