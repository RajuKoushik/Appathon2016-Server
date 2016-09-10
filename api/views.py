from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
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
        age = request.POST.get('age')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            user = User(user_name = user_name, password = password, email=email,
                    first_name = first_name, last_name = last_name, age = age)
            user.save()

            resp = functions.Response()
            resp.add('user_name', user_name)

            return resp.respond()
        except Exception as e:
            print(e)
            return functions.user_exists()
    else:
        return functions.invalid_option()

    """
    Login a user
    """

    @csrf_exempt
    def login(request):
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            user = User.objects.filter(username=user_name, password=password)
            if len(user) == 1:
                resp = functions.Response()
                cuser = user[0]
                resp.add('id', cuser.id)
                resp.add('firstname', cuser.firstName)
                resp.add('lastname', cuser.lastName)
                resp.add('email', cuser.email)
                resp.add('username', cuser.username)
                posts = Post.objects.filter(user=cuser)
                postitles = []
                posttexts = []
                postvotes = []

                counter = 0
                for i in posts:
                    postitles[counter] = i.post_name
                    posttexts[counter] = i.post_text
                    postvotes[counter] = i.post_votes
                resp.add('posttitles',postitles)
                resp.add('postexts',posttexts)
                resp.add('postvotes',postvotes)
                return resp.respond()

            else:
                return functions.auth_failed()
        else:
            return functions.invalid_option()