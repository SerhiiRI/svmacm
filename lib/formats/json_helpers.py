from lib.static.authentication.encryption import \
    encode , \
    decode
from functools import \
    wraps, \
    reduce
from flask import \
    json, \
    request, \
    Response


def JSON(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    return decorator

def RESP(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        value = f(*args, **kwargs)
        resp = Response(value if type(value) == "str" else str(value))
        resp.content_type = "application/json"
        return resp
    return decorator


@RESP
@JSON
def JSONError(
        error: int = 404,
        message: str = "",
) -> dict:
    return {
        "error": error,
        "description": message,
    }

def JSONSaveUserList(key, userList:list):
    userList = [dict({"login":log, "password":passwd}) for log, passwd in userList]
    with open("users.file", "w+") as authfile:
        authfile.write(encode(key, json.dumps(userList)))


def JSONVerifiedUser(key, login:str, password:str) -> bool:
    with open("users.file", "r") as authfile:
        dictionary = json.loads(decode(key, authfile.read()))
        for dic in dictionary:
            if (str(dic["login"]) == login and str(dic["password"]) == password):
                return True
        return False


def _JSONvalidation(request_template: dict, comparing_template: dict):
    compare = lambda acc, key: acc \
               and (key in comparing_template) \
               and ((type(request_template[key]) is type(comparing_template[key])))
    return reduce(compare, request_template.keys(), True)


def JSONValidation(*templates):
    def infuntionWraper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            print("--------------> START VALIDATOR <------------")
            if request.is_json == True:
                if reduce(
                        (lambda acc, valid: acc or _JSONvalidation(request.get_json(), valid))
                        , templates
                        , False) :
                    return f(*args, **kwargs)
                else:
                    return JSONError(500, "User Json Validation ERROR")
                    print("--------------> VALIDATOR ERROR <------------")
            else:
                return f(*args, **kwargs)

        return decorator
    return infuntionWraper