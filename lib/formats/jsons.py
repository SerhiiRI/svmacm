from lib.formats.json_helpers import JSON, RESP


@RESP
@JSON
def JSONSuccess():
    return {
        "message" : "success"
    }

@RESP
@JSON
def JSONKey(key):
    return {
        "key" : str(key)
    }


@RESP
@JSON
def JSONMessage(keyvalue: list):
    d = dict()
    for k, v in keyvalue:
        d[str(k)] = v
    return d


_login_login_template = {
    "login": "",
    "password": ""
}
_login_key_template = {
    "key": ""
}
_container_template = {
    "key": "",
    "id": "",
    "function": ""
}
_containers_templates = {
    "key": "",
    "type": "",
    "function": ""
}
_image_template = {
    "key": "",
    "image": "",
    "function": ""
}
_images_template = {
    "key": "",
    "type": "",
    "function": ""
}
_logout_template = {
    "key": ""
}

JSONUserTPLT = dict()
JSONUserTPLT["login_login"] = _login_login_template
JSONUserTPLT["login_key"] = _login_key_template
JSONUserTPLT["container"] = _container_template
JSONUserTPLT["containers"] = _containers_templates
JSONUserTPLT["image"] = _image_template
JSONUserTPLT["images"] = _images_template
JSONUserTPLT["logout"] = _logout_template
