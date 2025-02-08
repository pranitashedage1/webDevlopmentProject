from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('ajax_user_search/', views.ajax_user_search, name='ajax_user_search'),
]