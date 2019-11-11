''' Contains all the cart view.'''

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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


def add_to_cart(request, slug):
    '''Retrive the product and the cart then feed to the
    CartItem.Then update the cartitem and the cart.'''

    # retrive the product
    product = retrived_product(slug)
    
    # retrive the cart
    cart = retrived_cart(request)

    # Feeding to the CartItem
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # update cartitem and cart
    update_cartitem(request, cart_item)
    update_cart_total(request, cart)

    return HttpResponseRedirect(reverse('cart'))


def remove_from_cart(request, pk):
    cart = retrived_cart(request)
    cart_item = CartItem.objects.filter(cart=cart, pk=pk)
    cart_item.delete()
    # message
    update_cart_total(request, cart)

    return HttpResponseRedirect(reverse('cart'))


def update_cart_item(request):
    '''Update cart Item quantity and also variations(still not applied) from the cart.'''

    
    pk = request.GET.get('pk')
    cart_item = CartItem.objects.get(pk=pk)

    if int(request.GET.get('qty')) <= 0:
        cart_item.delete()
        cart = retrived_cart(request)
        update_cart_total(request, cart)
        cart_total = cart.total
        return JsonResponse({
            'id': pk,
            'product': 'empty',
            'cart_total': cart_total
        })
        
    cart_item.quantity = request.GET.get('qty')
    cart_item.save()
    cart = retrived_cart(request)
    update_cart_total(request, cart)

    if request.is_ajax():
        line_total = CartItem.objects.get(pk=pk).line_total
        cart_total = cart.total
        print('hi')
        return JsonResponse({
            'line_total': line_total,
            'cart_total': cart_total
        })
    
    return HttpResponseRedirect(reverse('cart'))
