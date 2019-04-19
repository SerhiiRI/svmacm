from functools import wraps
from flask import request, Response
from lib.static.template.jsons import \
    JSONVerifiedUser , \
    JSONSaveUserList , \
    JSONError
import random
import json
import string

class UserManager(object):

    def __init__(self):
        self.key = self.__generate_key()
        self.__initialize_users()
        self.__user_id = list()

    def __generate_key(self, length:int, login=None):
        k = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])
        (login and self.__user_id.append((login, k)))
        return k

    def __error401_NotVarifyAccess(self):
        return JSONError(401, "Not verified access to resource")

    def __verify_key(self, key):
        for log, ukey in self.__user_id:
            if ukey == key: return key
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


    def authenticate(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            dictionary = json.dumps(request.get_json())
            if("userloginkey" in dictionary):
                return f(*args)
                getKey(JSONVerifiedUser())
            else:
                error401_NotVarifyAccess()
            return f(*args, **kwargs)
        return decorator()


    def __initialize_users(self):
        users = [
            ("admin", "admin"),
            ("serhii", "admin"),
            ("marcin","admin")]
        JSONSaveUserList(key, users)



key=getKey()