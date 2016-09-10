from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from .models import *

"""
Login a user
"""


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = User.objects.filter(user_name=user_name, password=password)
        if len(user) == 1:
            resp = functions.Response()
            cuser = user[0]

            resp.add('firstname', cuser.first_name)
            resp.add('lastname', cuser.last_name)
            resp.add('email', cuser.email)
            resp.add('user_name', cuser.user_name)
            posts = Post.objects.all()
            postitles = []
            posttexts = []
            postvotes = []

            counter = 0
            for i in posts:
                postitles[counter] = i.post_name
                posttexts[counter] = i.post_text
                postvotes[counter] = i.post_votes
                counter = counter + 1
            resp.add('posttitles', postitles)
            resp.add('postexts', posttexts)
            resp.add('postvotes', postvotes)
            return resp.respond()

        else:
            return functions.auth_failed()
    else:
        return functions.invalid_option()


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


def addpost(request):
    if request.method == 'POST':
        post_name = request.POST.get('post_name')
        post_text = request.POST.get('post_text')
        post_tag = request.POST.get('post_tag')
        post_catid = request.POST.get('post_catid')
        user_name = request.POST.get('user_name')
        try:
            post = Post(post_name=post_name,post_text=post_text,post_tag=post_tag,post_catid=post_catid,user_id = User.objects.filter(user_name=user_name))
            post.save()



            resp = functions.Response()

            posts = Post.objects.all()
            postitles = []
            posttexts = []
            postvotes = []

            counter = 0
            for i in posts:
                postitles[counter] = i.post_name
                posttexts[counter] = i.post_text
                postvotes[counter] = i.post_votes
                counter = counter + 1
            resp.add('posttitles', postitles)
            resp.add('postexts', posttexts)
            resp.add('postvotes', postvotes)

            return resp.respond()
        except Exception as e:
            print(e)
            return functions.user_exists()
    else:
        return functions.invalid_option()

def catpost(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        post_catid = request.POST.get('post_catid')
        post = Post.objects.filter(post_catid=post_catid)


        resp = functions.Response()



        resp.add('user_name', user_name)

        postitles = []
        posttexts = []
        postvotes = []

        counter = 0
        for i in post:
            postitles[counter] = i.post_name
            posttexts[counter] = i.post_text
            postvotes[counter] = i.post_votes
            counter = counter + 1
        resp.add('posttitles', postitles)
        resp.add('postexts', posttexts)
        resp.add('postvotes', postvotes)
        return resp.respond()
    else:
        return functions.invalid_option()







