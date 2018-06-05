from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Question
from .models import *


def index(request):
    if request.method == "POST":
        request
    return render(request, 'main.html')


def goods(request):
    goods_to_show = Good.objects.all()
    if request.method == "POST":
        cat = request.POST['choice']
        if cat != "Все": goods_to_show = Good.objects.filter(category__category_name=cat)
    cats = Category.objects.all()
    context = {'goods' : goods_to_show,
               'cats' : cats}
    return render(request, 'goods.html', context)


def good(request, good_id):
    item = Good.objects.filter(id=int(good_id)).get()
    context = { 'good' : item }
    return render(request, 'good.html', context)


def auth(request):
    return render(request, 'auth.html')

def reg(request):
    return render(request, 'reg.html')
