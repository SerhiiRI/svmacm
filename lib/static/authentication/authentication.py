from functools import wraps
from flask import request, Response



def __check_auth(username, password):
    return username == "admin" and password == "admin"

def getKey():
    return "jad4432hjs7o23n18n"

def error401_NotVarifyAccess():
    return "error Request"

def authenticate(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        dictionary = request.get_json()
        dictionary = dict()
        if("login" in dictionary and "password" in dictionary):
            getKey()
        else:
            error401_NotVarifyAccess()
        return f(*args, **kwargs)
    return decorator()