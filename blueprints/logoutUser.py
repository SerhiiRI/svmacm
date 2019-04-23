from flask import Blueprint, Flask, Response, abort
from flask import json, request, render_template, make_response, redirect, url_for
from lib.static.authentication.authentication import\
    clean_key , \
    authenticate

from lib.formats.jsons import JSONError

#flask = Flask(__name__)

logoutUser = Blueprint(name='logoutTemplate', import_name=__name__, template_folder='templates')


@logoutUser.route('/logout', methods=["GET"])
@authenticate
def logout(key):
    resp = Response()
    resp.mimetype = "plain/text"
    resp.status_code = 302
    resp.location = "/"
    if(key != None):
        resp.set_cookie("key", "", expires=0)
        clean_key(key)
    return resp
