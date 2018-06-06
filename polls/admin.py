from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class StashItemDisplay(admin.ModelAdmin):
    list_display = ('user', 'item')
    #list_filter = ['user']
    search_fields = ['user__user_name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Good)
admin.site.register(User)
admin.site.register(Component)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(StashItem, StashItemDisplay)
