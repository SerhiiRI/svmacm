from flask import Blueprint, Flask, Response, abort
from flask import json, request, render_template, make_response
from lib.static.authentication.authentication import authenticate
from lib.formats.jsons import JSONError

#flask = Flask(__name__)

renderMain = Blueprint(name='renderMain', import_name=__name__, template_folder='templates')


@renderMain.route('/', methods=["POST", "GET"])
@authenticate
def svmacm(key="12341"):
    if(request.content_type == "application/json"):
        backValue = json.dumps([{
        "temporarykey": key,
        "type": "container",
        "name": "temp",
        "id" : 123321,
        "network" : {
            "received" : 1332321,
            "transceived" : 111111,
            "unit" : "MB"
        },
        "cpu": 1,
        "ram": 12,
        "image": {
            "name" : "fedora",
            "version": "version"
            },
        "status" : "ACTIVE"
        }])
        resp = Response(backValue)
        resp.content_type = "application/json"
        return resp
    print(request.method, request.content_type, request.method == "GET")
    if (key == None):
        resp = make_response(render_template("index.html", type="user"))
        # resp = make_response(render_template("containers.html", type="user"))
        return resp
    else:
        print(key)
        resp = make_response(render_template("index.html", type="admin"))
        resp.set_cookie("key", key)
        # resp = make_response(render_template("containers.html", type='admin'))
        # resp.set_cookie("key", "", expires=0)
        return resp
    #return abort(500)
