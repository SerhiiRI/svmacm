from flask import Blueprint, Response

from lib.formats.json_helpers import JSONValidation, RESP, JSON, JSONError
from lib.formats.jsons import JSONUserTPLT
from lib.static.authentication.authentication import\
    clean_key , \
    authenticate


@RESP
@JSON
def JSONLogoutSuccess() -> dict:
    return {
        "logout" : "success"
    }

logoutUser = Blueprint(name='logoutTemplate', import_name=__name__)

@logoutUser.route('/logoutHTML', methods=["GET"])
@authenticate
def logoutHTML(key):
    resp = Response()
    resp.mimetype = "plain/text"
    resp.status_code = 302
    resp.location = "/"
    if(key != None):
        resp.set_cookie("key", "", expires=0)
        clean_key(key)
    return resp


@logoutUser.route('/logoutJSON', methods=["POST"])
@JSONValidation(JSONUserTPLT["logout"])
@authenticate
def logoutJSON(key):
    if(key != None):
        clean_key(key)
        return JSONLogoutSuccess()
    return JSONError(500, "not found user")

