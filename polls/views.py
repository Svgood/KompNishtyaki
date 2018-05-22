from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question
from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ',\n '.join([q.question_text for q in latest_question_list])
    context = {'question' : latest_question_list}
    return render(request, 'main.html', context)


def goods(request):
    goods_to_show = Good.objects.all()
    cat = None
    if request.method == "POST":
        cat = request.POST['choice']
    if cat is not None and cat != "Все":
        goods_to_show = Good.objects.filter(category__category_name=cat)
    cats = Category.objects.all()
    context = {'goods' : goods_to_show,
               'cats' : cats}
    return render(request, 'goods.html', context)

def good(request, good_id):
    item = Good.objects.filter(id=int(good_id)).get()
    context = { 'good' : item }
    return render(request, 'good.html', context)

def detail(request, question_id):
    return HttpResponse("You are looking at question {}".format(question_id))


def results(request, question_id):
    return HttpResponse("You are looking at the results of question {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("You are voting on question {}".format(question_id))