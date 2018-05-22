from django.contrib import admin

from .models import *



class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Good)
admin.site.register(User)
admin.site.register(Component)
admin.site.register(Order)
admin.site.register(Category)
