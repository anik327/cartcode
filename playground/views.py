from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import ExpressionWrapper
from django.db.models import Q
from store.models import Product


def say_hello(request):
    # queryset = Product.objects.filter(title__istartswith="coffee").values()
    queryset = Product.objects.filter(Q(unit_price__lte=40) | Q(unit_price__gte=20))
    # print(product)
    return render(request, "hello.html", {"name": "Anik", "result": queryset})
