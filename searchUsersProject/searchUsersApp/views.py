from django.http import JsonResponse
from django.shortcuts import render
from .models import Users

def index(request):
    return render(request, 'searchUsersApp/index.html')

def users(request):
    return render(request, 'searchUsersApp/users.html')

def ajax_user_search(request):
    query = request.GET.get('q', '').strip()  # Safely get the query parameter
    if query:
        users = Users.objects.filter(first_name__icontains=query)
        user_list = [{'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users]
        return JsonResponse(user_list, safe=False)
    return JsonResponse([], safe=False)
