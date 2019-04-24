from functools import wraps
from flask import Flask, request, Response
from lib.formats.jsons import \
    JSONVerifiedUser , \
    JSONSaveUserList , \
    JSONError
import random
import json
import pprint
import string
FlaskSerwer = Flask(__name__)
p = pprint.PrettyPrinter()

def __generate_key(length: int, login=None):
    k = "".join([random.choice(string.ascii_letters + string.digits) for d in range(length)])
    if login : __user_id[login] = k
    return k


def __error401_NotVarifyAccess():
    resp = Response(JSONError(401, "Not verified access to resource"))
    resp.content_type = "application/json"
    FlaskSerwer.process_response(resp)
    return resp


def __error401_NotCorrectLogin():
    resp = Response(JSONError(401, "Login are not correct"))
    resp.content_type = "application/json"
    FlaskSerwer.process_response(resp)
    return resp


def __verify_key(key):
    for log, ukey in __user_id.items():
        if ukey == key: #return key
            return key
    return False


def clean_key(key):
    for log, ukey in __user_id.items():
        if ukey == key: #return key
            __user_id.pop(log)
            break
    return False


def __verify_login(login, password):
    if (JSONVerifiedUser(__key, login, password)):
        return (__generate_key(10, login))
    return False


def __authentifiation__service__error():
    resp = Response(JSONError(500, "internal server error"))
    resp.content_type = "application/json"
    FlaskSerwer.process_response(resp)
    return resp


def authenticate(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        p.pprint(__user_id)
        print("=> Login ",end='')

        if(request.content_type == "application/json"):
            print("=> JSON", end='')
            dictionary = request.get_json()
            if "key" in dictionary:
                print(" => key {}".format(dictionary["key"]), end='')
                key = __verify_key(dictionary["key"])
                if key:
                    print(" => key is verified ", end='')
                    return f(key)

            if "login" in dictionary and "password" in dictionary:
                print(dictionary["login"], dictionary["password"], end='')
                key = __verify_login(dictionary["login"], dictionary["password"])
                if(key):
                    print(" => key is verified {} ".format(key), end='')
                    return f(key)
            print('____________________________________/')
            return f(None)

        else:
            print(" => HTML", end='')

            if("key" in request.cookies.keys()):
                print(" => cookies [{}]".format(request.cookies.get("key")), end='')
                key = __verify_key(request.cookies.get("key"))
                print(key)
                if key:
                    print(" => key is verified", end='')
                    return f(key=key, *args, **kwargs)

            if("login" in request.form.keys() and "password" in request.form.keys()):
                print(" => post form login ", end='')
                print("FORM LOGIN: "+request.form.get("login"), " PASSWORD: "+request.form.get("password"))
                key = __verify_login(request.form.get("login"), request.form.get("password"))
                print(key)
                if (key):
                    print(" => login is verified", end='')
                    return f(key=key, *args, **kwargs)

        return f(key=None)
    return decorator


def __initialize_users():
    users = [
        ("admin", "admin"),
        ("serhii", "admin"),
        ("marcin","admin")]
    JSONSaveUserList(__key, users)

__key = __generate_key(10)
__initialize_users()
__user_id = dict()