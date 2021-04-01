from django.shortcuts import render
from django.http import HttpResponse

from first_page.models import User

def save(request, name, age, add, marks):
    u = User(name = name, age = age, add = add, marks = marks)
    u.save()
    return HttpResponse("POST query")


def get_all(request):
    u = User.objects.all()
    users = [i.name for i in u]
    resp = ','.join(users)
    return HttpResponse(resp)

def get_data(request, name):
    u = User.objects.get(name = name)
    return HttpResponse(u.name)

def delete(request, name):
    u = User.objects.get(name = name)
    u.delete()
    return HttpResponse("Delete Call")

def count(request):
    u = User.objects.count()
    return HttpResponse(u)

def Pass(request):
    u = User.objects.all()
    users = [i.name for i in u if i.marks>75]
    return HttpResponse(users)