from django.shortcuts import render, redirect
from .models import *
def dashboard(request):
    context = {
        "course": Course.objects.all(),
        "link": Link.objects.all(),
    }
    return render(request, 'index.html', context)

def mock(request):
    context = {
        "mock": Mock.objects.filter(status=1),
        "link": Link.objects.all(),
    }
    return render(request, 'mock.html', context)

def addstudent(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    cource = request.POST.get('course')

    Student.objects.create(name=name, phone_number=phone_number, cource=Course.objects.get(id=cource))

    return redirect("success")
def addstudent_mock(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    mock = request.POST.get('mock')

    Student.objects.create(name=name, phone_number=phone_number, mock=Mock.objects.get(id=mock))

    return redirect("success")


def success(request):
    return render(request, "admins/page-404.html")