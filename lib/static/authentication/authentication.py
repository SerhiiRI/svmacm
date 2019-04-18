import base64
from functools import wraps
from flask import request, Response
import random
import string


def __check_auth(username, password):
    return username == "admin" and password == "admin"

def getKey():
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
    #return "jad4432hjs7o23n18n"

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


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return str(base64.urlsafe_b64encode(bytes("".join(enc), "UTF-8")))


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


key = "serhiiBMF"


with open("users.file", "w+") as authfile:
    authfile.write(encode(key, (JSONTemplate("admin", "lala"))))

def addUser():
    with open("user.fiel", "rw+") as file:
        if file


def TestUser(key, login, password):
    with open("users.file", "r") as authfile:
        dictionary = json.loads(decode(key, authfile.read()))
        return (dictionary["login"]    == login and
                dictionary["password"] == password)

print("LOGIN:{}".format(str(testuser(key, "admin", "lala"))))


