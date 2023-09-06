from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    all_carousel = Carrossel.objects.all()
    all_depoi = Depoi.objects.all()
    all_infor = Infor.objects.all()
    all_offers = Offer.objects.all()
    all_products = Products.objects.all()
    return render(request,'index.html',{"carro": all_carousel, "depoi": all_depoi, "info": all_infor, "offer": all_offers, "prod": all_products})

def sobre(request):
    return render(request, 'about.html')

def livro(request):
    return render(request,'book.html')

def menu(request):
    return render(request,'menu.html')
