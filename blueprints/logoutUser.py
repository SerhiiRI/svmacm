from flask import Blueprint, Flask, Response, abort
from flask import json, request, render_template, make_response, redirect, url_for
from lib.formats.jsons import JSONError, JSONMessage
from lib.static.authentication.authentication import\
    clean_key , \
    authenticate


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
@authenticate
def logoutJSON(key):
    if(key != None):
        clean_key(key)
        resp = Response(JSONMessage([("logout", "afasd")]))
        resp.content_type = "application/json"
        return resp
    resp = Response(JSONError(500, "bad request"))
    resp.content_type = "application/json"
    return resp

