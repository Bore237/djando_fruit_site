from django.shortcuts import render
from .models import Product
from django.http  import  HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("just to best") retourne un message sous forme html
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})