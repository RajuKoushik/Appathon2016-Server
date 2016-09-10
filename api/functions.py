from django.http import HttpResponse
import json
from .models import User


def checkUserCredentials(request):
    uid = request.POST.get('id')
    password = request.POST.get('password')
    user = User.objects.filter(id=uid, password=password)
    if len(user) == 0:
        return False
    else:
        return True

"""
Responses
"""
def auth_failed(code = 302, msg = 'Authentication Problem'):
    return send_response(code, msg)

def invalid_option(code = 404, msg = 'Invalid Option'):
    return send_response(code, msg)

def error_happened(code = 400, msg = 'Bad things have happened'):
    return send_response(code, msg)

def user_exists(code = 301, msg = 'User already exists'):
    return send_response(code, msg)

def send_response(code = 200, msg = 'OK'):
    a = Response(code)
    a.add('message', msg)
    return a.respond()

"""
Return a
Response
"""
class Response:
    def __init__(self, code=200):
        self.json = {}
        self.json['code'] = code

    def add(self, key, value):
        self.json[key] = value

    def respond(self):
        return HttpResponse(json.dumps(self.json), content_type='application/json')