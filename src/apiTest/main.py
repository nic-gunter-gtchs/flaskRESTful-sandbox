from fmLib import fileman as FM
from flask import Flask, request
from flask_restx import Api, Resource

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
        ext = request.form["data"]["extension"]
        pass
      case "update":
        path = request.form["data"]["directory"]
        write = request.form["data"]["writable"]
        pass
      case "supdate":
        path = request.form["data"]["directory"]
        format = request.form["data"]["special"]
        pass
      return {"data": fmresp}
  
if __name__ == '__main__':
    app.run(debug=True)
