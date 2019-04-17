from django.db import models

class AskQuestion(models.Model):
    questionid = models.AutoField(primary_key=True)
    questionTitle = models.CharField(max_length=100)
    questionText = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questionTitle

class QuestionAnswer(models.Model):
    questionid = models.ForeignKey(AskQuestion,on_delete=models.CASCADE)
    answerid =  models.AutoField(primary_key=True)
    answerText = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
