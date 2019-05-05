from multiprocessing import Pool
import json

from flask import Blueprint, Response
from flask import request, render_template, make_response
from lib.ContainerController import ContainerController
from lib.dockerAPI.container_function import \
    containerStatus, \
    cpuPercentUsage, \
    networkUsage, \
    memoryRAM, \
    imageNameTag, \
    containerNameId
from lib.formats.json_helpers import JSONValidation
from lib.static.authentication.authentication import authenticate
from lib.formats.json_helpers import JSON, RESP, JSONError
from lib.formats.jsons import \
    JSONUserTPLT, \
    JSONSuccess, \
    JSONMessage, \
    GetHelp


@RESP
@JSON
def JSONContainers(
        containers: list,
) -> list:
    def getJSONContainerTemplate(container):
        STATDICT = container.stats(stream=False)
        image, version = imageNameTag(container)
        status = containerStatus(container)
        name, container_id = containerNameId(STATDICT)
        if(status=="running"):
            receive, transceive = networkUsage(STATDICT, 'MB')
            cpu = cpuPercentUsage(STATDICT)
            memory = memoryRAM(STATDICT)
            unit = "KB"
            return JSONContainersTemplate(
                    name=name,
                    container_id=container_id,
                    receive=receive,
                    transceive=transceive,
                    unit=unit,
                    cpu=cpu,
                    memory=memory,
                    image=image,
                    version=version,
                    status=status
                )
        else:
            return JSONContainersTemplateMinimize(
                name=name,
                container_id=container_id,
                image=image,
                version=version,
                status=status
            )
    return list(map(getJSONContainerTemplate, containers))


def JSONContainersTemplateMinimize(
        name="-",
        container_id=0,
        image="-",
        version="-",
        status="not exist") -> dict:
    return {
        "type": "container",
        "name": name,
        "id": container_id,
        "id_short": container_id[:10],
        "image": {
            "name": image,
            "version": version
        },
        "status": status
    }

def JSONContainersTemplate(
        name="-",
        container_id=0,
        receive=0,
        transceive=0,
        unit="B",
        cpu=0,
        memory=0,
        image="-",
        version="-",
        status="not exist") -> dict:
    return {
        "type": "container",
        "name": name,
        "id": container_id,
        "id_short":container_id[:10],
        "network": {
            "received": receive,
            "transceived": transceive,
            "unit": unit
        },
        "cpu": cpu,
        "ram": memory,
        "image": {
            "name": image,
            "version": version
        },
        "status": status
    }

# TODO Refactor this pfease of shit
def DICTContainers(
        containers: list,
) -> list:
    def getJSONContainerTemplate(container):
        STATDICT = container.stats(stream=False)
        image, version = imageNameTag(container)
        status = containerStatus(container)
        name, container_id = containerNameId(STATDICT)
        if (status == "running"):
            receive, transceive = networkUsage(STATDICT, 'MB')
            cpu = cpuPercentUsage(STATDICT)
            memory = memoryRAM(STATDICT)
            unit = "KB"
            return JSONContainersTemplate(
                name=name,
                container_id=container_id,
                receive=receive,
                transceive=transceive,
                unit=unit,
                cpu=cpu,
                memory=memory,
                image=image,
                version=version,
                status=status
            )
        else:
            return JSONContainersTemplateMinimize(
                name=name,
                container_id=container_id,
                image=image,
                version=version,
                status=status
            )
    return list(map(getJSONContainerTemplate, containers))

__Container_Controller = ContainerController()

containerRoute = Blueprint(name           ='containers',
                           import_name    =__name__    ,
                           template_folder='templates' )


@containerRoute.route('/containers', methods=["POST", "GET"])
@JSONValidation(JSONUserTPLT["login_key"], JSONUserTPLT["container"], JSONUserTPLT["containers"])
@authenticate
def getContainers(key=None):
    if(request.content_type == "application/json"):
        request_data_dictionary = request.get_json()
        if len(request_data_dictionary.keys()) == 1 and "key" in request_data_dictionary:
            return GetHelp("/containers")
        return getJsonResponce(request_data_dictionary)
    else:
        if (key != None):
            Containers = __Container_Controller.list()
            print(Containers)
            s = DICTContainers(Containers)
            resp = make_response(render_template("containers.html", type="admin", key=key, containers=s))
            resp.set_cookie("key", key)
            return resp
    resp = Response()
    resp.mimetype = "plain/text"
    resp.status_code = 302
    resp.location = "/"
    return resp



def getJsonResponce(request_data:dict):
    function = request_data["function"]
    if("id" in request_data):
        if (None == __Container_Controller.get(request_data["id"])):
            return JSONError(500, "container not found")
        if (function == "start"):
            return JSONSuccess() if __Container_Controller.start_container(request_data["id"]) else JSONError(500, "container stop error")
        if (function == "stop"):
            return JSONSuccess() if __Container_Controller.stop_container(request_data["id"]) else JSONError(500, "container stop error")
        if (function == "remove"):
            return JSONSuccess() if __Container_Controller.delete(request_data["id"]) else JSONError(500, "Container remove error ")
        if (function == "info"):
            Container = __Container_Controller.get(request_data["id"])
            if (Container):
                return JSONContainers([Container])
            else:
                return JSONError(500, "bad container ID")
        return JSONError(1, "None defined function")
    if("type" in request_data):
        if (function == "startall"):
            return JSONSuccess() if __Container_Controller.start_all_containers() else JSONError(500, "containers stop error")
        if (function == "stopall"):
            return JSONSuccess() if __Container_Controller.stop_all_containers() else JSONError(500, "containers stop error")
        if (function == "removeall"):
            return JSONSuccess() if __Container_Controller.remove_all_containers() else JSONError(500,"Containers remove error ")
        if(function == "list"):
            Containers = __Container_Controller.list()
            print(Containers)
            if(len(Containers) > 0):
                return JSONContainers(Containers)
            elif len(Containers) == 0 :
                return JSONMessage([("containers", "[]")])
            else:
                return JSONError(500, "Container API crash")
    return JSONError(0, "None defined request")


@containerRoute.route('/containers_', methods=["POST"])
@JSONValidation(JSONUserTPLT["login_key"], JSONUserTPLT["container"], JSONUserTPLT["containers"])
@authenticate
def getContainersAjax(key=None):

    if(request.content_type == "application/json" and key != None):
        print("=====",request.get_json())
        return getHTMLResponce(request.get_json())
    if(key == None):
        return "/container_ route please login"
    return "/container_ : Not correct request handling"


def getHTMLResponce(request_data:dict):
    function = request_data["function"]
    if("id" in request_data):
        if (None == __Container_Controller.get(request_data["id"])):
            return JSONError(500, "container not found")
        if (function == "start"): __Container_Controller.start_container(request_data["id"])
        if (function == "stop"): __Container_Controller.stop_container(request_data["id"])
        if (function == "remove"): __Container_Controller.delete(request_data["id"])
    if("type" in request_data):
        if (function == "startall"): __Container_Controller.start_all_containers()
        if (function == "stopall"):__Container_Controller.stop_all_containers()
        if (function == "removeall"):__Container_Controller.remove_all_containers()
    Containers = __Container_Controller.list()
    print(Containers)
    if(len(Containers) == 0):
        return "Empty containers list"
    s = DICTContainers(Containers)
    resp = make_response(render_template("container_table_template.html", containers=s))
    return resp