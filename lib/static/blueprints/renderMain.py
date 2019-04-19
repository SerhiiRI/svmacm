from flask import Blueprint, Flask, Response
from flask import json, request
from lib.static.authentication.authentication import authenticate
flask = Flask(__name__)


renderMain = Blueprint('renderMain', __name__, template_folder='templates')

@renderMain.route('/', method="POST")
@serviceHTMLType('/')
@authenticate
def svmacm(key):
    """
    backValue = {}
    if not request.is_json:
        backValue = json.dumps(
            {
                "error": "request does not of Json Type",
                "instruction": "http://localhost/instruction"
            })
    else:
    """
    if(true):
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
    flask.process_response(resp)
    return resp
