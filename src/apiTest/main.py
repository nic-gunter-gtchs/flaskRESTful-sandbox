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
        fmresp = FM.newF(fname, dir, ext)
      case "read":
        path = request.form["data"]["directory"]
        fmresp = FM.readF(path)
      case "supdate":
        path = request.form["data"]["directory"]
        format = request.form["data"]["special"]
        fmresp = FM.readS(path, format)
    if fmresp == False:
      return {"error": "Malformed request"}, 405
    else:
      return {"data": fmresp}
  
if __name__ == '__main__':
    app.run(debug=True)
