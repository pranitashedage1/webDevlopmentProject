from django.urls import path

from . import views

print("url2")
urlpatterns = [
    # path("", views.index, name="index"),
    # path("help/", views.help, name="help")
    path("", views.index, name="index"),
    # path("users/", views.users, name="users")
]

