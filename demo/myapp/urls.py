from django.urls import path
from . import views

# here is where we will do the routing
urlpatterns = [
    # empty path is the root path
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
]