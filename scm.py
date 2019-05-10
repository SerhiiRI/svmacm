#!/usr/bin/python3
from flask import Flask
import os


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





scm.run(debug=True, host="0.0.0.0", port=8777)
# httpserver = WSGIServer(('0.0.0.0', 8777), scm)
# httpserver.serve_forever()
