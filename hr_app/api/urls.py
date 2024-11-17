from django.urls import path
from .views import get_users, create_user, user_detail

urlpatterns = [
    path("users/", get_users, name=get_users.__name__),
    path("users/create/", create_user, name=create_user.__name__),
    path("users/<int:pk>", user_detail, name=user_detail.__name__),
]
