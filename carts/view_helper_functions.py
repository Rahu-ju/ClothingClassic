from products.models import Product
from carts.models import Cart


# retrive the product
def retrived_product(slug):
    try:
        product = Product.objects.get(slug=slug)
        return product
    except Product.DoesNotExists:
        pass
    except:
        pass

# retrive cart
def retrived_cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)

    return cart

def update_cart_total(request, cart):

    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        item.line_total = line_total
        item.save()
        new_total += line_total
    cart.total = new_total
    cart.save()

    request.session['items_total'] = cart.cartitem_set.count()

# update cart item from the post form
def update_cartitem(request, cart_item):
    if request.method == 'POST':
        size = request.POST.get('size')
        type = request.POST.get('type')
        color = request.POST.get('color')
        items = request.POST.get('items')

        if int(items) >= 0:
            cart_item.size = size
            cart_item.type = type
            cart_item.color = color
            cart_item.quantity = items
            cart_item.save()
        else:
            cart_item.delete()