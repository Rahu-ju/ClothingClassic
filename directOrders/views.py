from django.shortcuts import render

# Create your views here.
def direct_checkout(request):
    template = 'checkout/direct_order_checkout.html'
    context = {}
    return render(request, template, context)


def order_confirm(request):
    template = 'checkout/order_confirm.html'
    context = {}
    return render(request, template, context)