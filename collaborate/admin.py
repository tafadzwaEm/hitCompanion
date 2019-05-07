from django.contrib import admin
from .models import *

class AskQuestionAdmin(admin.ModelAdmin):
    list_display = ('questionTitle','timestamp')
    list_filter = ('timestamp',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback','timestamp')
    list_filter = ('timestamp',)

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(AskQuestion,AskQuestionAdmin)
admin.site.register(QuestionAnswer)

admin.site.site_header = 'hitCompanion Administration Dashboard'

# Register your models here.
