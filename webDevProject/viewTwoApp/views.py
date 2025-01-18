from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'viewTwoApp/index.html', context=my_dict)

def help(request):
    help_dir = {'help_insert':"Hello page "}
    return render(request, 'viewTwoApp/help.html', context=help_dir)

