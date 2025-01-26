from django.shortcuts import render
from viewTwoApp.models import User

# Create your views here.

# def index(request):
#     my_dict = {'insert_me': "Hello I am from views.py!"}
#     return render(request, 'viewTwoApp/index.html', context=my_dict)

# def help(request):
#     help_dir = {'help_insert':"Hello page "}
#     return render(request, 'viewTwoApp/help.html', context=help_dir)

def index(request):
    return render(request, 'viewTwoApp/index.html')

def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'usersList': users_list}
    return render(request, 'viewTwoApp/users.html', context=user_dict)
