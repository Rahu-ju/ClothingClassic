import uuid

from django.http import HttpResponseRedirect
from django.urls import reverse

from orders.models import Order
from carts.models import Cart


# generate unique order id
def order_id_generator():
    order_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    # checking the order already exist or not
    try:
        Order.objects.get(id=order_id)
        order_id_generator()
    except:
        return order_id

# Another way to genetrate id 
import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in size)
    return the_id


# retrieve cart
def retrieve_cart():
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    return cart

# create order
def create_order(cart, request):
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

    return new_order

