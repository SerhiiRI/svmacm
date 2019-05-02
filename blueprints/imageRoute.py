import json

from flask import Blueprint
from flask import request, render_template, make_response

from blueprints.containerRoute import JSONContainers
from lib.ImageController import ImageController
from lib.static.authentication.authentication import authenticate
from lib.formats.json_helpers import \
    JSONValidation, \
    JSON, \
    RESP, \
    JSONError
from lib.formats.jsons import \
    JSONUserTPLT, \
    JSONSuccess, \
    JSONMessage, \
    GetHelp

__Image_Controller = ImageController()
__image_functionality = {
    "pull": __Image_Controller.pull,
    "run": __Image_Controller.run,
    "delete": __Image_Controller.delete,
    "get": __Image_Controller.getByName
}

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

def JSONImageTemplate(image: str = "",version: str = "") -> dict:
    return {
        "type": "image",
        "name": image,
        "version": version
    }

@RESP
@JSON
def JSONImageTemplateByImage(image) -> dict:
    try:
        imagename, tag = image.tags[0].split(":")
    except Exception:
        imagename, tag = image.tags[0], "-"
    return {
        "type": "image",
        "name": imagename,
        "version": tag
    }

@RESP
@JSON
def JSONImages(images: list):
    return [[JSONImageTemplate(*version.split(":")) for version in image.tags ]for image in images]

# > renderMain - główny blueprint
# odpowiedzialny za generacje strony
# tytulowej. Ona zawiera dokumentacje

imageRoute = Blueprint(name           ='images',
                       import_name    =__name__    ,
                       template_folder='templates' )


@imageRoute.route('/images', methods=["POST", "GET"])
@JSONValidation(JSONUserTPLT["login_key"], JSONUserTPLT["image"], JSONUserTPLT["images"], JSONUserTPLT["image_tag"])
@authenticate
def getImages(key=None):
    if(request.content_type == "application/json"):
        request_data_dictionary = request.get_json()
        if len(request_data_dictionary.keys()) == 1 and "key" in request_data_dictionary:
            return GetHelp("/images")
        return getJsonResponce(request_data_dictionary)
    else:
        print(request.method, request.content_type, request.method == "GET")
        if (key != None):
            resp = make_response(render_template("index.html", type="admin", key=key))
            resp.set_cookie("key", key)
            return resp
    resp = make_response(render_template("index.html", type="user"))
    return resp


def getJsonResponce(request_data:dict):
    function = request_data["function"]
    if("image" in request_data):
        tag = request_data["tag"] if ("tag" in request_data) else "latest"
        imagename = request_data["image"] if ":" in request_data["image"] else "{}:{}".format(request_data["image"],
                                                                                              tag)
        if (function == "pull"):
            if request_data["tag"] == "all":
                tag = None
            return JSONSuccess() if __Image_Controller.pull(request_data["image"], tag=tag) else JSONError(500, "Image Pull Crash")
        if (function == "delete"):
            return JSONSuccess() if __Image_Controller.delete(imagename) else JSONError(500, "Image Pull Crash")
        if (function == "get"):
            Image = __Image_Controller.getByName(imagename)
            if (Image):
                return JSONImageTemplateByImage(Image)
            else:
                return JSONError(500, "image '{}' not been found. ot found image or specyfic image Tag".format(imagename))
        if (function == "run"):
            Container = __Image_Controller.run(imagename)
            if(Container):
                return JSONContainers([Container])
            else:
                return JSONError(500, "you can not run that container")
        return JSONError(1, "None defined function")
    if("type" in request_data):
        if(function not in ["deleteall", "list"]):
            return JSONError(500, "function '{}' is not defined in SCM API".format(function))
        if (function == "deleteall"):
            return JSONSuccess() if __Image_Controller.delete_all() else JSONMessage([("describe", "force delete is crashed")])
        if(function == "deleteall"):
            return JSONSuccess() if __Image_Controller.prune() else JSONMessage([("describe", "not available containers, or api error")])
        if(function == "list"):
            Images = __Image_Controller.list()
            if(Images):
                return JSONImages(Images)
            else:
                return JSONMessage([("images", "[]")])
    return JSONError(0, "None defined exception")

