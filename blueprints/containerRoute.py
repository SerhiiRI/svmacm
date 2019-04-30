from multiprocessing import Pool
import json

from flask import Blueprint
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
    JSONUserTPLT, JSONSuccess, JSONMessage


@RESP
@JSON
def JSONContainers(
        containers: list,
) -> list:
    def getJSONContainerTemplate(container):
        STATDICT = container.stats(stream=False)
        receive, transceive = networkUsage(STATDICT, 'MB')
        name, container_id = containerNameId(STATDICT)
        cpu = cpuPercentUsage(STATDICT)
        memory = memoryRAM(STATDICT)
        image, version = imageNameTag(container)
        status = containerStatus(container)
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
    return list(map(getJSONContainerTemplate, containers))



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

__Container_Controller = ContainerController()

containerRoute = Blueprint(name           ='containers',
                           import_name    =__name__    ,
                           template_folder='templates' )


@containerRoute.route('/containers', methods=["POST", "GET"])
@JSONValidation(JSONUserTPLT["container"], JSONUserTPLT["containers"])
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
    print("======ERROR")
    resp = make_response(render_template("index.html", type="user"))
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
            Container = __Container_Controller.run(request_data["container"])
            if (Container):
                return JSONContainers(list(Container))
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
                return JSONMessage([("containers", "[]ш")])
            else:
                return JSONError(500, "Container API crash")
    return JSONError(0, "None defined request")

