from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import *


def index(request):
    response = render(request, 'main.html')
    if request.method == "POST":
        response = HttpResponseRedirect(reverse('index'))
        if "log" in request.POST:
            log = request.POST["login"]
            pas = request.POST["pas"]
            user = User.objects.filter(user_name=log, user_password=pas)
            if len(user) == 1:
                response.set_cookie("login", log)
                response.set_cookie("password", pas)
                response.set_cookie("buy", 0)
        if "exit" in request.POST:
            response.delete_cookie("login")
            response.delete_cookie("password")
            response.delete_cookie("buy")
        return response
    return response


def goods(request):
    goods_to_show = Good.objects.all()
    if request.method == "POST":
        response = HttpResponseRedirect(reverse('goods'))

        cat = request.POST['choice']
        if cat != "Все": goods_to_show = Good.objects.filter(category__category_name=cat)
    cats = Category.objects.all()
    context = {'goods' : goods_to_show,
               'cats' : cats}
    return render(request, 'goods.html', context)


def good(request, good_id):
    item = Good.objects.filter(id=int(good_id)).get()
    context = {'good': item}
    response = render(request, 'good.html', context)

    if request.method == "POST":
        response = HttpResponseRedirect(reverse('index'))
        response.set_cookie("buy", int(request.COOKIES.get('buy')) + 1)

    return response


def auth(request):
    return render(request, 'auth.html')


def reg(request):
    return render(request, 'reg.html')
