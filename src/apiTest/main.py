from fmLib import fileman as FM
from flask import Flask, request
from flask_restx import Api, Resource
from markupsafe import escape

app = Flask(__name__)
api = Api(app)

@api.route("/tests/fm/api")
class FileMan(Resource):
  def put(self):
    type = request.form["data"]["type"]
    match type:
      case "create":
        dir = request.form["data"]["directory"]
        fname = request.form["data"]["name"]
        
        pass
      case "update":
        
