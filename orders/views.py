from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order
from .view_helper_functions import order_id_generator
from carts.models import Cart

# Create your views here.
def checkout(request):
    '''Retrieve the cart from session, create order, run credit card,
    delete cart from the session.'''

    #Checking the cart
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))

    # Create the order
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = order_id_generator()
        new_order.save()
    except:
        # error message
        return HttpResponseRedirect(reverse('cart'))

    # assign address
    # run credit card
    # del cart from the session when order is finfished by admin.
    if new_order.status == 'Finished':
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse('cart'))

    context = {}
    template = 'checkout/checkout1.html'
    return render(request,template, context)

    
def orders(request):
    '''Show all orders '''
    context = {}
    template = 'orders/customer-orders.html'
    return render(request, template, context)


def order_detail(request):
    '''Show specefic order daetail'''
    context = {}
    template = 'orders/customer-order.html'
    return render(request, template, context)