#!/usr/bin/python3
import os
#import json
from flask import Flask

# ENV['TRASHPANDA_HOST'] = "trashpanda.pwsz.nysa.pl"
# ENV['CLOUD_MAX_FILE_SIZE'] = '1MB'
# ENV['CLOUD_PROJECT_PATH'] = os.getcwd()
# ENV['CLOUD_TRASHBOX'] = '/srv/Data/'
# ENV['TRASHPANDA_LOGIN'] = ENV['TRASHPANDA_LOGIN'] if 'TRASHPANDA_LOGIN' in ENV else "sergiy1998"
# ENV['TRASHPANDA_PASSWD'] = ENV['TRASHPANDA_PASSWD'] if 'TRASHPANDA_PASSWD' in ENV else "hspybxeR98>"

from blueprints.renderMain import renderMain
from blueprints.logoutUser import logoutUser
from blueprints.imageRoute import imageRoute
from blueprints.containerRoute import containerRoute

scm = Flask(__name__)
scm.secret_key = os.urandom(24)

scm.register_blueprint(renderMain)
scm.register_blueprint(imageRoute)
scm.register_blueprint(logoutUser)
scm.register_blueprint(containerRoute)




# keys = []
#
# def myPrint(*args, **kwargs):
#     print("IMAGES:")
#     print("\n".join(["\t"+"\t=> ".join(str(str(x).split("'")[1]).split(":")) for x in args]))

# pprinter = PrettyPrinter()
# img = ImageController(myPrint)
# cntr = ContainerController(myPrint)

# cntr.start_all_containers()
#
# print(__name__)

# HTML API


# @flask.route('/', methods=["GET"])
# def index():
#     return htmlindex
    #username = request.cookies.get("username")

# @flask.route('/', methods=["POST"])
# def index():
#     backValue = ""
#     if request.is_json:
#         backValue = json.dumps([{
#             "type": "container",
#             "name": "temp",
#             "id": 123321,
#             "network": {
#                 "received": 1332321,
#                 "transceived": 111111,
#                 "unit": "MB"
#             },
#             "cpu": 1,
#             "ram": 12,
#             "image": {
#                 "name": "fedora",
#                 "version": "version"
#             },
#             "status": "ACTIVE"
#         }])
#         authorisation = request.get_json()
#         print(authorisation["login"])
#         print(authorisation["password"])
#     resp = Response(backValue)
#     resp.content_type = "application/json"
#     flask.process_response(resp)
#     return resp
    #username = request.cookies.get("username")

# @flask.errorhandler(404)
# def page_not_found(e):
#     return error404, 404 #render_template('404.html'), 404
#
# # JSON API
# @flask.route('/', methods=['POST'])
# def gerRespond():
#     return ""


# def getContainers():
#     listContainers = cntr.list()
#     pprint()
#     #return json.dump()





# container = img.run("fedora")
# container = img.run("haskell")
# container = img.run("clojure")
# container = img.run("fedora")
# listContainers = cntr.list()
# print("======proceses======")
#cntr.stats_container(listContainers[0].name)




# d = cntr.stats_container(listContainers[0].name)
# name, id = containerNameId(d)
# print("---> Name {} id {}...".format(name, id[0:10]))
# print("---> NETWORK Recieved {0} {2} Send: {1} {2}".format(*networkUsage(d, 'MB'),"MB"))
# print("---> CPU {}%".format(str(cpuPercentUsage(d))))
# print("---> Memory {}%".format(str(memoryRAM(d))))
# print("---> container {} v: {}".format(*imageNameTag(listContainers[0])))
# print("---> Status: {}".format(containerStatus(listContainers[0])))
# lllist = [{
#         "type": "container",
#         "name": "temp",
#         "id" : 123321,
#         "network" : {
#             "received" : 1332321,
#             "transceived" : 111111,
#             "unit" : "MB"
#         },
#         "cpu": 1,
#         "ram": 12,
#         "image": {
#             "name" : "fedora",
#             "version": "version"
#         },
#         "status" : "ACTIVE"
#     }]
# for x in listContainers:
#     stat = cntr.stats_container(x.name)
#     name, id = containerNameId(stat)
#     receive, transceive = networkUsage(stat, "MB")
#     cpu = cpuPercentUsage(stat)
#     memory = memoryRAM(stat)
#     image, version = imageNameTag(x)
#     status = containerStatus(x)
#     lllist.append({
#         "type": "container",
#         "name": name,
#         "id" : id,
#         "network" : {
#             "received" : receive,
#             "transceived" : transceive,
#             "unit" : "MB"
#         },
#         "cpu": cpu,
#         "ram": memory,
#         "image": {
#             "name" : image,
#             "version": version
#         },
#         "status" : status
#     })
# cntr.stats_container(listContainers[0].name)
# # print("========stats=======")
# cntr.proces_container(listContainers[0].name)
# # print("========logs========")
# cntr.logs_container(listContainers[0].name)
# pprinter.pprint(listContainers[0].image.tags)

# imagelist = img.list()
# pprinter.pprint(str(imagelist[0].tags).split(':'))

# cntr.stop_all_containers()
# cntr.start_all_containers()
# cntr.status_all_containers()
# cntr.remove_all_containers()

# cntr.list()

# cntr.prune_container()


import socket, errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

scm.run(debug=True, host="0.0.0.0", port=8777)
# httpserver = WSGIServer(('0.0.0.0', 8777), scm)
# httpserver.serve_forever()
