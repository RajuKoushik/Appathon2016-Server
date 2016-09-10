from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
rom . import functions
from .models import *





"""
Registers a user
"""
@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name') # None default if no second param
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        try:
            user = User(user_name = user_name, password = password, email=email,
                    first_name = first_name, last_name = last_name)
            user.save()
            uid = user.id
            resp = functions.Response()
            resp.add('user_name', user_name)
            resp.add('id', uid)
            return resp.respond()
        except Exception as e:
            print(e)
            return functions.user_exists()
    else:
        return functions.invalid_option()