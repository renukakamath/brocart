from django.shortcuts import render

# Create your views here.
from product.models import *

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required






def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')
    context={
        'featured_products': featured_products,
        'latest_products': latest_products
        
    }
    
  
    
    return render(request,'index.html',context)

@login_required(login_url='/account/')
def product_list(request):
    page=1    #paginator
    if request.GET:  #paginator
        page=request.GET.get('page',1) #paginator
        
    product_list=Product.objects.order_by('priority')
    
    product_paginator=Paginator(product_list,4) #paginator
    product_list=product_paginator.get_page(page) #paginator
    
    context={'product_list': product_list}
    return render(request,'product_list.html',context)

@login_required(login_url='/account/')
def detail_product_list(request,pk):
    
    product_detailslist=Product.objects.get(pk=pk)
    context={'product_detailslist':product_detailslist}
    return render(request,'detail_product_list.html',context)
