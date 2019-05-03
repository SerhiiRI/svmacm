from flask import Blueprint
from flask import request, render_template, make_response

from lib.formats.json_helpers import JSONValidation
from lib.static.authentication.authentication import authenticate
from lib.formats.jsons import JSONUserTPLT, GetHelp
from lib.formats.json_helpers import \
    JSON, \
    RESP, JSONError


# > JSONxxxx - lista funkcyj związana
# z szablonami odpowiedzi dla JSON-typu
# danych
@RESP
@JSON
def JSONKey(
        key:str
    ) -> dict:
    return {
        "key" : key
    }

@RESP
@JSON
def JSONGetMainPage(route:bool=None, key:str=None) -> dict:
    pathDICT = lambda path, desc: {"route": path, "describe": desc}
    MainDictionary = {
        "title": "SCM",
        "about": "Server kontroli systemu wirtualizacji docker, korzystując z abstrakcji sterowania, zorganizowanej w podstaowych mechanizmach Docker API",
        "author": "Marcin Ochocinski",
        "poweredBy":"Serioża",
        }
    if (route):
        MainDictionary["routes"] = [
            pathDICT("/", "plain text about program and some of information"),
            pathDICT("/containers", "JSON containers manipulation route"),
            pathDICT("/images", "JSON images manipulation route"),
            pathDICT("/logoutJSON", "logout path")
        ]
    if (key):
        MainDictionary["key"] = key
    return MainDictionary

# > renderMain - główny blueprint
# odpowiedzialny za generacje strony
# tytulowej. Ona zawiera dokumentacje

renderMain = Blueprint(name           ='renderMain',
                       import_name    =__name__    ,
                       template_folder='templates' )


@renderMain.route('/', methods=["POST", "GET"])
@JSONValidation(JSONUserTPLT["login_login"], JSONUserTPLT["login_key"])
@authenticate
def svmacm(key=None):
    if(request.content_type == "application/json"):
        return JSONGetMainPage() if key == None else GetHelp()
    else:
        print(request.method, request.content_type, request.method == "GET")
        if (key != None):
            resp = make_response(render_template("index.html", type="admin", key=key))
            resp.set_cookie("key", key)
            return resp
    resp = make_response(render_template("index.html", type="user"))
    return resp

