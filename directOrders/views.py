from django.shortcuts import render

from .forms import DirectOrderForm

# Create your views here.
def direct_checkout(request):
    # prefill the user form.
    # process submitted form data
    if request.method == "POST":
        pass
    else:
        form = DirectOrderForm


    template = 'checkout/direct_order_checkout.html'
    context = {"form": form}
    return render(request, template, context)


def order_confirm(request):
    template = 'checkout/order_confirm.html'
    context = {}
    return render(request, template, context)