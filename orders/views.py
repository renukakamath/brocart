from django.shortcuts import render,redirect
from orders.models import Order,OrderItem
from product.models import Product
from django.contrib import messages

# Create your views here.
def showcart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
        
    )
    context={'cart':cart_obj}
    
    return render(request,'cart.html',context)


def add_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile

       
        quantity = int(request.POST.get('quantity')) 
        product_id = request.POST.get('product_id')

        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        ) 
        product=Product.objects.get(pk=product_id)   
        order_item, created = OrderItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )

       
        if created:
            order_item.quantity = quantity
        else:
            order_item.quantity += quantity
            order_item.save()

        
   
    return redirect('cart')


def remove_cart_item(request,pk):
    item=OrderItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')



def checkout_order(request):
    try:
        if request.POST:
            user = request.user
            customer = user.customer_profile
            totals = float(request.POST.get('total'))  # Make sure 'total' is coming from the frontend

            # Get the order object in the cart stage
            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )

            if order_obj:
                # Set the order to ORDER_CONFIRMED
                order_obj.order_status = Order.ORDER_CONFIRMED
                # Assign the total price to the order
                order_obj.total_price = totals
                # Save the order object with the updated status and total price
                order_obj.save()
                status_message = "Your order is processed. Your item will be delivered within 2 days."
                messages.success(request, status_message)
            else:
                status_message = "Your order was not processed."
                messages.error(request, status_message)

    except Exception as e:
        status_message = "Your order was not processed."
        messages.error(request, status_message)

    # Redirect the user back to the cart page
    return redirect('cart')




    

    