from django.shortcuts import render

# Create your views here.
def posts(request):
    template = 'blog/posts.html'
    context = {}

    return render(request, template, context)


def post_detail(request):
    template ='blog/post_detail.html'
    context = {}

    return render(request, template, context)