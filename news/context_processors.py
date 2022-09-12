from news.models import News
from django.shortcuts import render

import random
from constance import config


def extras(request):
    # trending = list(News.objects.all())
    # trending = random.sample(trending, 3)

    trending = News.objects.order_by("-views")[:3]
    return {'trending': trending}


# def const(request):

#     return render(request, 'news/footer.html', {'config':config})


