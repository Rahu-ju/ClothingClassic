from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Order
from .forms import OrderAddressForm
from .utils import order_id_generator
from carts.models import Cart

# Create your views here.
def checkout(request):
    '''Retrieve the cart from session, create order, run credit card,
    delete cart from the session and from the database.'''

    #retrieve the cart
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))

    # retrieve the product items  from the cart
    product_items = cart.cartitem_set.all
        

    if request.method == "POST":
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
    else:
        form = OrderAddressForm()
    
    context = {"form": form, 
               "product_items": product_items, }
    
    template = 'checkout/direct_order_checkout.html'
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