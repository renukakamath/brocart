from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def product_list(request):
    return render(request,'product_list.html')

def detail_product_list(request):
    return render(request,'detail_product_list.html')
