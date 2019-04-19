from lib.dockerAPI.container_function import \
    containerStatus , \
    cpuPercentUsage , \
    networkUsage    , \
    memoryRAM       , \
    imageNameTag    , \
    containerNameId
from lib.static.authentication.encryption import \
    encode , \
    decode
from multiprocessing import Pool
from functools       import wraps
from flask           import json


def JSON(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    return decorator()


@JSON
def JSONContainers(
        containers:list,
    ) -> list:
    def getJSONContainerTemplate(container):
        STATDICT            = container.stats          (stream =False)
        receive, transceive = networkUsage             (STATDICT,'MB')
        name, container_id  = containerNameId          (STATDICT)
        cpu                 = cpuPercentUsage          (STATDICT)
        memory              = memoryRAM                (STATDICT)
        image, version      = imageNameTag             (container)
        status              = containerStatus          (container)
        unit                = "KB"
        return JSONContainersTemplate(
            name          = name,
            container_id  = container_id,
            receive       = receive,
            transceive    = transceive,
            unit          = unit,
            cpu           = cpu,
            memory        = memory,
            image         = image,
            version       = version,
            status        = status
        )
    return Pool().map(getJSONContainerTemplate, containers)


@JSON
def JSONImages(
        images:list
    ) -> list:
    return [
        JSONImageTemplate(*str(image.tags)
                          .split(':'))
        for   image
        in    images]


def JSONContainersTemplate(
    name          = "-",
    container_id  = 0,
    receive       = 0,
    transceive    = 0,
    unit          = "B",
    cpu           = 0,
    memory        = 0,
    image         = "-",
    version       = "-",
    status        = "not exist") -> dict:
    return {
        "type"    : "container",
        "name"    : name,
        "id"      : container_id,
        "network" : {
            "received"    : receive,
            "transceived" : transceive,
            "unit"        : unit
        },
        "cpu"    : cpu,
        "ram"    : memory,
        "image"  : {
            "name"    : image,
            "version" : version
        },
        "status" : status
    }


def JSONImageTemplate(
        image:  str = "",
        version:str = ""
    ) -> dict:
    return {
        "type"   : "image",
        "name"   : image,
        "version": version
    }


@JSON
def JSONError(
    error:int    = 404,
    message:str  = "",
    other        = 0
    ) -> dict:
    return {
        "error"    : error,
        "message"  : message,
        "other"    : other
    }


@JSON
def JSONKey(
        key:str
    ) -> dict:
    return {
        "key" : key
    }

def JSONSaveUserList(key, userList:list):
    userList = [dict({"login":log, "password":passwd}) for log, passwd in userList]
    print(userList)
    with open("users.file", "w+") as authfile:
        authfile.write(encode(key, json.dumps(userList)))

def JSONVerifiedUser(key, login, password):
    with open("users.file", "r") as authfile:
        dictionary = json.loads(decode(key, authfile.read()))
        return (dictionary["login"]    == login and
                dictionary["password"] == password)