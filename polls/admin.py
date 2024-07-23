from django.contrib import admin
from .models import Question, Choice, ChoiceVote

class ChoiceVoteInline(admin.TabularInline):
    model = ChoiceVote
    extra = 1

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # Number of extra empty choices to display

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceVoteInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(ChoiceVote)
