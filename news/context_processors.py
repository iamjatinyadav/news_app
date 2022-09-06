from news.models import News
import random
from constance import config
from django.shortcuts import render


def extras(request):
    # trending = list(News.objects.all())
    # trending = random.sample(trending, 3)

    trending = News.objects.order_by("-views")[:3]
    return {'trending': trending}


def const(request):
    return {'config':config}