from django.shortcuts import render, HttpResponse
from .models import TodoItem


# create your views here
def home(requests):
    return render(requests, "home.html")


def todos(requests):
    items = TodoItem.objects.all()
    return render(requests, "todos.html", {
        "todos": items
    })
