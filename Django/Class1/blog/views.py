from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(
        request,
        "blog/blog.html"
    )

def exemple(request):
   return render(
        request,
        "blog/exemple.html"
    )
