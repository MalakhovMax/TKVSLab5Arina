from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import AddOwn

# Create your views here.
def creator(request):
    if request.method == "POST":
        ord = Own()
        ord.name = request.POST.get("name")
        ord.tour = request.POST.get("tour")
        ord.date = request.POST.get("date")
        ord.phone = request.POST.get("phone")
        ord.address = request.POST.get("address")
        ord.save()
        return HttpResponseRedirect("/")
    else:
        AddForm = AddOwn()
        return render(request, "creator.html", {"form": AddForm})

def orders(request):
    ord = Own.objects.all()
    return render(request, "orders.html", {"ord": ord})

def mainpage(request):
    return render(request, "mainpage.html")