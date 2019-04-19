from functools import wraps
from flask import Flask, request, Response
from lib.static.template.jsons import \
    JSONVerifiedUser , \
    JSONSaveUserList , \
    JSONError
import random
import json
import string

FlaskSerwer = Flask(__name__)

class UserManager(object):

    def __init__(self):
        self.__key = self.__generate_key()
        self.__initialize_users()
        self.__user_id = dict()

    def __generate_key(self, length:int, login=None):
        k = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])    
        (login and self.__user_id[login] = k))
        return k

    def __error401_NotVarifyAccess(self):
        resp = Response(JSONError(401, "Not verified access to resource"))
        resp.content_type = "application/json"
        FlaskSerwer.process_response(resp)
        return resp
    
    def __error401_NotCorrectLogin(self):
        resp = Response(JSONError(401, "Login are not correct"))
        resp.content_type = "application/json"
        FlaskSerwer.process_response(resp)
        return resp

    def __verify_key(self, key):
        for log, ukey in self.__user_id:
            if ukey == key: #return key
                return __generate_key(10, log)
        return False

    def __verify_user(self, dictionary):
        return (
            (("temporarykey" in dictionary)
              and
             (self.__verify_key(dictionary["temporarykey"])))

                     or

            ((("login" in dictionary) and ("password" in dictionary))
              and
             (JSONVerifiedUser(self.key, dictionary["login"], dictionary["password"]))
              and
             (self.__generate_key(dictionary["login"])))
        )
    
    def __verify_login(self, login, password):
        if not (JSONVerifiedUser(self.__key, dictionary["login"], dictionary["password"])):
            return (self.__generate_key(dictionary["login"]))
        return False              
             
    
    def __authentifiation__service__error(self):
        resp = Response(JSONError(500, "internal server error"))
        resp.content_type = "application/json"
        FlaskSerwer.process_response(resp)
        return resp

    def authenticate(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            dictionary = json.dumps(request.get_json())
            if("temporarykey" dictionary):
                if(__verify_key):
                    return f(key, *args, **kwargs)
                else:
                    return __error401_NotVarifyAccess(*args, **kwargs)
            if("login" in dictionary and "password" in dictionary):
                key = serlf.__verify_login(dictionary["login"], dictionary["password"])
                if(key):
                    return f(key, *args, **kwargs)
                else:
                    return __error401_NotCorrectLogin(*args, **kwargs)
             return __authentifiation__service__error()
                    
        return decorator()


    def __initialize_users(self):
        users = [
            ("admin", "admin"),
            ("serhii", "admin"),
            ("marcin","admin")]
        JSONSaveUserList(key, users)



key=getKey()
