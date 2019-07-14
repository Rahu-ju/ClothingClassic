''' Contains all the cart view.'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from products.models import Product
from .models import Cart, CartItem
from .view_helper_functions import retrived_product,retrived_cart, update_cart_total, update_cartitem


def view(request):
    '''Get the cart id from the session, retrive the cart
    from the database and then pass it to the context dict.'''

    # retrive cart from session, making context, render
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}
    else:
        context = {'empty': True}
    
    template = 'carts/cart.html'
    return render(request, template, context)


def update_cart(request, slug):
    '''Retrive the product and the cart then feed to the
    CartItem.Then update the cartitem and the cart.'''

    # retrive the product
    product = retrived_product(slug)
    
    # retrive the cart
    cart = retrived_cart(request)

    # Feeding to the CartItem
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    update_cartitem(request, cart_item)
    update_cart_total(request, cart)

    return HttpResponseRedirect(reverse('cart'))



