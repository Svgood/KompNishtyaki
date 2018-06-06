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
                stashItems = StashItem.objects.filter(user=user.get())
                response.set_cookie("buy", len(stashItems))
        if "exit" in request.POST:
            response.delete_cookie("login")
            response.delete_cookie("password")
            response.delete_cookie("buy")
        return response
    return response


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
    context = {'good': item}
    response = render(request, 'good.html', context)

    if request.method == "POST":
        user = User.objects.filter(user_name=request.COOKIES.get("login")).get()
        good = Good.objects.filter(id=int(good_id)).get()
        response = HttpResponseRedirect(reverse('index'))
        newStash = StashItem(user=user, item=good)
        newStash.save()
        response.set_cookie("buy", len(StashItem.objects.filter(user=user)))

    return response


def basket(request):
    user = User.objects.filter(user_name=request.COOKIES.get("login")).get()
    stashItems = StashItem.objects.filter(user=user)
    goods = []
    for item in stashItems:
        goods.append(item.item)
    context = {"goods" : goods}
    return render(request, 'basket.html', context)

def deleteFromBasket(request, good_id):
    user = User.objects.filter(user_name=request.COOKIES.get("login")).get()
    stash = StashItem.objects.filter(user=user, item_id=good_id)
    for s in stash:
        s.delete()
        break
    respons = HttpResponseRedirect(reverse('index'))
    respons.set_cookie("buy",  len(StashItem.objects.filter(user=user)))
    return respons

def auth(request):
    return render(request, 'auth.html')


def reg(request):
    return render(request, 'reg.html')
