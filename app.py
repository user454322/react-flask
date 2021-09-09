from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
#from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
#app = Flask(__name__, static_url_path='', static_folder=os.path.abspath('frontend/build'))
#CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    app.logger.warning('Accessing %s', path)
    app.logger.warning('Static folder %s', app.static_folder)
    return send_from_directory(static_folder, index.html')

api.add_resource(HelloApiHandler, '/flask/hello')

