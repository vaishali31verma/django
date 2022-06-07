
from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from django.views import generic
# Create your views here.
# Create your views here.
from math import ceil
def index(request):
    products=product.objects.all()
    print(products)

    n=len(products)
    nSlides= n//4 + ceil((n/4) -(n//4))
    params = {'no_of_slide': nSlides ,'product' : products,'range':range(1,nSlides)}
    return render(request,'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return HttpResponse("contactus")
def Tracker(request):
    return HttpResponse("Tracker")
def search(request):
    return HttpResponse("search")
def prodView(request):
    return HttpResponse("prodView")

def checkout(request):
    return HttpResponse("checkout")

