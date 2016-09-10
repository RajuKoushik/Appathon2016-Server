from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

from .models import *


"""
Login a user
"""
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if len(user) == 1:
            resp = functions.Response()
            cuser = user[0]
            resp.add('id', cuser.id)
            resp.add('firstname', cuser.firstName)
            resp.add('lastname', cuser.lastName)
            resp.add('email', cuser.email)
            resp.add('username', cuser.username)
            subscriptions = UserSubscription.objects.filter(user=cuser)
            subs = []
            for i in subscriptions:
                d = {}
                d['subsid'] = i.id
                d['searchparam'] = i.searchParam
                d['links'] = []
                subLinks = SubscriptionLink.objects.filter(userSub=i)
                for row in subLinks:
                    d2 = dict()
                    d2['url'] = row.link.url
                    d2['name'] = row.link.name
                    d2['pid'] = row.link.pid
                    d2['network'] = row.link.network
                    d['links'].append(d2)
                subs.append(d)

            resp.add('subscriptions', subs)
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
        username = request.POST.get('username') # None default if no second param
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')
        try:
            user = User(username = username, password = password, email=email,
                    firstName = firstName, lastName = lastName)
            user.save()
            uid = user.id
            resp = functions.Response()
            resp.add('username', username)
            resp.add('id', uid)
            return resp.respond()
        except Exception as e:
            print(e)
            return functions.user_exists()
    else:
        return functions.invalid_option()