from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Product
from django.contrib import messages
from rest_framework import viewsets, permissions
from myapp.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("/db")


def update(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.save()
        messages.success(request, "Data updated successfully")
        return redirect("/db")

    product = Product.objects.get(id=product_id)
    return render(request, "form_update.html", {"product": product})


def add(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']

        product = Product.objects.create(name=name, price=price)
        product.save()
        messages.success(request, "Data added sucessfully")
        return redirect("/db")

    return render(request, "form_add.html")


def db(request):
    all_products = Product.objects.all
    some_products = Product.objects.filter(price__gt=5000)
    return render(request, "db.html", {"all_products": all_products, "some_products": some_products})


def index(request):
    name = 'อนุสรณ์ บรรเทิง'
    age = 42
    return render(request, "index.html", {"name": name, "age": age})


def hello(request):
    return HttpResponse("<h1>Hello</h1>")
