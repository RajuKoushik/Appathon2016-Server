from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from . import functions
from .models import *
from . import feeds

"""
Gets the Main feed for an user
"""
@csrf_exempt
def getMainFeed(request):
    if request.method != 'POST':
        return functions.invalid_option()
    uid = request.POST.get('id')
    user = User.objects.filter(id=uid)
    feedData = feeds.getCacheForUser(user[0])
    resp = functions.Response()
    resp.add('feeds', feedData)
    return resp.respond()