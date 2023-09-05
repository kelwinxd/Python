
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return HttpResponse('Blog Page from app 1')

def exemple(request):
    print('exemple')
    return HttpResponse('exemplo do app 1')
