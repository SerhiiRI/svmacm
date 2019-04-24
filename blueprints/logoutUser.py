from flask import Blueprint, Flask, Response, abort
from flask import json, request, render_template, make_response, redirect, url_for
from lib.formats.jsons import JSONError
from lib.static.authentication.authentication import\
    clean_key , \
    authenticate


#flask = Flask(__name__)

logoutUser = Blueprint(name='logoutTemplate', import_name=__name__, template_folder='templates')


@logoutUser.route('/logoutHTML', methods=["GET"])
@authenticate
def logoutHTML(key):
    resp = Response()
    resp.mimetype = "plain/text"
    resp.status_code = 302
    resp.location = "/"
    resp.content_type = "application/json"
    if(key != None):
        resp.set_cookie("key", "", expires=0)
        clean_key(key)
    return resp

@logoutUser.route('/logoutJSON', method=["POST"])
@authenticate
def logoutJSON(key):
    if(key != None):
        clean_key(key)
        return
    return JSONError(500, "server crash")

