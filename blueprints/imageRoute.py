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
    JSONUserTPLT, JSONSuccess, JSONMessage

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


def JSONImageTemplateByImage(image) -> dict:
    try:
        image, tag = image.tags[0].split(":")
    except Exception:
        image, tag = image.tags[0], "-"
    return {
        "type": "image",
        "name": image,
        "version": tag
    }

@RESP
@JSON
def JSONImages(images: list) -> list:
    return [
        JSONImageTemplate(*str(image.tags)
                          .split(':'))
        for image
        in images]

# > renderMain - główny blueprint
# odpowiedzialny za generacje strony
# tytulowej. Ona zawiera dokumentacje

imageRoute = Blueprint(name           ='images',
                       import_name    =__name__    ,
                       template_folder='templates' )


@imageRoute.route('/images', methods=["POST", "GET"])
@JSONValidation(JSONUserTPLT["image"], JSONUserTPLT["images"])
@authenticate
def getImages(key=None):
    if(request.content_type == "application/json"):
        return getJsonResponce(request.get_json())
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
        if (function == "pull"):
            return JSONSuccess() if __Image_Controller.pull(request_data["image"]) else JSONError(500, "Image Pull Crash")
        if (function == "delete"):
            return JSONSuccess() if __Image_Controller.delete(request_data["image"]) else JSONError(500, "Image Pull Crash")
        if (function == "get"):
            Image = __Image_Controller.getByName(request_data["image"])
            if (Image):
                return JSONImages([Image])
            else:
                return JSONError(500, "Image Pull Crash")
        if (function == "run"):
            Container = __Image_Controller.run(request_data["image"])
            if(Container):
                return JSONContainers([Container])
            else:
                return JSONError(500, "you can not run that container")
        return JSONError(1, "None defined function")
    if("type" in request_data):
        if(function == "deleteall"):
            return JSONSuccess() if __Image_Controller.prune() else JSONMessage([("describe", "not available containers, or api error")])
        if(function == "list"):
            Images = __Image_Controller.list()
            if(Images):
                return JSONImages(Images)
            else:
                return JSONError(500, "Container API crash")
    return JSONError(0, "None defined exception")

