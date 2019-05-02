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
_image_template_tag = {
    "key": "",
    "image": "",
    "tag":"",
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
JSONUserTPLT["image_tag"] = _image_template_tag
JSONUserTPLT["images"] = _images_template
JSONUserTPLT["logout"] = _logout_template


@RESP
@JSON
def GetHelp(route:str = "/"):
    if (route == "/"): return {
        "about": "The latter two codes are NOT honoured by many terminal emulators. The only ones that I'm aware of that do are xterm and nxterm - even though the majority of terminal emulators are based on xterm code. As far as I can tell, rxvt, kvt, xiterm, and Eterm do not support them. They are supported on the console. Try putting in the following line of code at the prompt (it's a little clearer what it does if the prompt is several lines down the terminal when you put this in): echo -en  This should move the cursor seven lines up screen, print the word , and then return to where it started to produce a normal prompt. This isn't a prompt: it's just a demonstration of moving the cursor on screen, using colour to emphasize what has been done. Save this in a file called :lorem fsdajfdoifqweoinfoieqonfenofdsa sdjf alds fjdsio foiwqem cofefrejowmaofmodm foasfdmodsam fodasf oas fmoimq wfnwofpneof wnidsoajfoidsm ",
        "routes": [
            {"/" : ""},
            {"sfad":"sad"},
            {"/conainers":""}
        ],
        "request" : [],
        "responds" : []
    }
    if (route == "/containers"): return{
        "about": "The latter two codes are NOT honoured by many terminal emulators. The only ones that I'm aware of that do are xterm and nxterm - even though the majority of terminal emulators are based on xterm code. As far as I can tell, rxvt, kvt, xiterm, and Eterm do not support them. They are supported on the console. Try putting in the following line of code at the prompt (it's a little clearer what it does if the prompt is several lines down the terminal when you put this in): echo -en  This should move the cursor seven lines up screen, print the word , and then return to where it started to produce a normal prompt. This isn't a prompt: it's just a demonstration of moving the cursor on screen, using colour to emphasize what has been done. Save this in a file called :lorem fsdajfdoifqweoinfoieqonfenofdsa sdjf alds fjdsio foiwqem cofefrejowmaofmodm foasfdmodsam fodasf oas fmoimq wfnwofpneof wnidsoajfoidsm ",
        "protocol": [{
            "key" : "key for confirming authentification",
            "type" : "type of requesting object from SCM API, by default 'containers'",
            "function" : "startall|stopall|removeall|list"
        },{
            "key" : "key for confirming authentification",
            "id" : "container id, for identification",
            "function" : "start|stop|remove|info"
        }],
        "examples": {
            "request":[
                {
                    "key": "654Fgefw3",
                    "type": "containers",
                    "function": "list"
                }, {
                    "key": "654Fgefw3",
                    "id": "jf439pj8jASDF432SGFgfsd231DSAfasdafds",
                    "function": "start"
                }
            ],
            "respond":[{
                "key": "sukabliatkey",
                "container": {
                    "type": "container",
                    "id": "asfj923b5479fhrawe9xpfj2x4x",
                    "name": "suk5in_syn",
                    "network": {
                        "received": 14297583,
                        "transceived": 660452,
                        "unit": "B"
                    },
                    "cpu": 10,
                    "ram": 1,
                    "image": {
                        "name": "fedora",
                        "version": "latest|3.5"
                    },
                    "status": "UP"
                    }
                }, {
                    "error": 500,
                    "message" : "to jebnie adam"
                }, {
                "message" : "success"
                }]
        }
    }
    if (route == "/images"): return {
        "about": "The latter two codes are NOT honoured by many terminal emulators. The only ones that I'm aware of that do are xterm and nxterm - even though the majority of terminal emulators are based on xterm code. As far as I can tell, rxvt, kvt, xiterm, and Eterm do not support them. They are supported on the console. Try putting in the following line of code at the prompt (it's a little clearer what it does if the prompt is several lines down the terminal when you put this in): echo -en  This should move the cursor seven lines up screen, print the word , and then return to where it started to produce a normal prompt. This isn't a prompt: it's just a demonstration of moving the cursor on screen, using colour to emphasize what has been done. Save this in a file called :lorem fsdajfdoifqweoinfoieqonfenofdsa sdjf alds fjdsio foiwqem cofefrejowmaofmodm foasfdmodsam fodasf oas fmoimq wfnwofpneof wnidsoajfoidsm ",
        "protocol": [{
            "key" : "key for confirming authentification",
            "type" : "default 'images'. Is type of requested JSON object, only for many images",
            "function" : "deleteall|prune|list"
        }, {
            "key" : "key for confirming authentification",
            "image" : "image name",
            "function" : "pull|run|delete|get"
        }],
        "examples": {
            "request":[
                {
                    "key": "654Fgefw3",
                    "type": "containers",
                    "function": "list"
                }, {
                    "key": "654Fgefw3",
                    "id": "jf439pj8jASDF432SGFgfsd231DSAfasdafds",
                    "function": "start"
                }
            ],
            "respond":[{
                "key": "sukabliatkey",
                "images": [ {
                    "type"   : "image",
                    "name"   : "fedora",
                    "version": "latest"
                },{
                    "type"   : "image",
                    "name"   : "haskell",
                    "version": "1.4"
                },{
                    "type"   : "image",
                    "name"   : "clojure",
                    "version": "3.4"
                }]
            }, {
                "error": 500,
                "message" : "to jebnie adam"
            }, {
                "message" : "success"
            }]
        }
    }
    return {
        "ERROR": "im fire... fire ... fireman and dancer... i am fire-fire-fireman and dancer"
    }