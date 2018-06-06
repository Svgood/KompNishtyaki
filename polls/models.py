from django.db import models
from django.utils import timezone

import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Good(models.Model):
    category = models.ManyToManyField(Category)
    good_name = models.CharField(max_length=200)
    good_description = models.TextField()
    good_cost = models.FloatField()
    good_img = models.ImageField(verbose_name="Photo", blank=True)
    good_img_link = models.CharField(max_length=255)

    def __str__(self):
        return self.good_name


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=255)
    user_lastname = models.CharField(max_length=200)
    user_email = models.CharField(max_length=255)
    user_birthDate = models.DateField()
    user_isAdmin = models.IntegerField(default=0)
    user_isBaned = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=255)
    order_date = models.DateField()
    order_cost = models.FloatField()


class Component(models.Model):
    component_name = models.CharField(max_length=255)
    component_description = models.TextField()


class StashItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Good, on_delete=models.CASCADE)

    def getUsername(self):
        return self.user.user_name
