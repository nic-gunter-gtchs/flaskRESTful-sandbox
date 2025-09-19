from fmLib import fileman as FM
from flask import Flask, request
from flask_restx import Api, Resource
import json
app = Flask(__name__)
api = Api(app)

@api.route("/tests/fm/api")
class FileMan(Resource):
  def put(self):
    data = request.get_json()
    mode = data['type']
    match mode:
      case "create":
        dir = data['directory'].strip()
        fname = data['name'].strip()
        ext = data['extension'].strip()
        fmresp = FM.newF(fname, dir, ext)
      case "read":
        path = data['directory'].strip()
        fmresp = FM.readF(path)
      case "supdate":
        path = data['directory'].strip()
        format = data['special'].strip()
        fmresp = FM.readS(path, format)
    if fmresp == False:
      return {"error": "Malformed request"}, 405
    else:
      return {"data": fmresp}
  
if __name__ == '__main__':
    app.run(debug=True)
