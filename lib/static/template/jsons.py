

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
    status        = "not exist"):
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