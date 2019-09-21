from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order
from .view_helper_functions import get_order_id

from carts.models import Cart
# Create your views here.
def checkout(request):
    '''checking the cart id, retrive the cart object, if not 
    redirect the cart page'''
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))

    '''Create the order'''
    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = get_order_id()
        new_order.save()


    context = {}
    template = 'checkout/checkout1.html'
    return render(request,template, context)