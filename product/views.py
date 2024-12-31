from django.shortcuts import render

# Create your views here.
from product.models import *

from django.core.paginator import Paginator


def index(request):
    return render(request,'index.html')


def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
        
    product_list=Product.objects.all()
    product_paginator=Paginator(product_list,4)
    product_list=product_paginator.get_page(page)
    context={'product_list': product_list}
    return render(request,'product_list.html',context)

def detail_product_list(request):
    
    product_list=Product.objects.all(pk=pk)
    return render(request,'detail_product_list.html')
