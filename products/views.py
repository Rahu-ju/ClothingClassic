from django.shortcuts import render
from django.http import Http404

from .models import Product

from marketing.models import Slider

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    try:
        cloths = Product.objects.filter(category='cloth')
        feature_cloth = cloths[0]
    except:
        feature_cloth = None

    # retrive liquid category product which has show_in_home_page property
    try:
        liquids = Product.objects.filter(category='liquid').filter(show_in_homepage=True)
        feature_liquid = liquids[0]
        print(liquids)
    except:
        feature_liquid = None
    
    template = 'homes/home.html'
    context = {"sliders": sliders, 
                "feature_cloth": feature_cloth,
                "feature_liquid": feature_liquid}
    return render(request, template, context)


def category(request):
    template = 'category/category.html'

    # retrive products from the database
    try:
        products = Product.objects.all()
        context = {'products': products }
        return render(request, template, context)
    except:
        raise Http404
    
def detail(request, slug):
    template = 'detail.html'

    # retrive the product(using slug) from the database
    try:
        product = Product.objects.get(slug=slug)
        items = product.variation_set.all()
        sizes = []
        types = []
        colors = []
        # taking all the feature of the product
        for item in items:
            if item.size:
                sizes.append(item.size)
            if item.type:
                types.append(item.type)
            if item.color:
                colors.append(item.color)

        context = {'product': product, 
                    'items': items, 
                    'sizes': sizes,
                    'colors': colors,
                    'types': types, }
        return render(request, template, context)
    except:
        raise Http404
