from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def customer(request):
    return HttpResponse("Customer")

def product(request):
    return HttpResponse("Product")