from fmLib import fileman as FM
from flask import Flask
from flask_restx import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
