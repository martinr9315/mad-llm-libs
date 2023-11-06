from flask import Flask
from madlibs import curate_madlibs
app = Flask(__name__)


@app.route("/api/madlibs", methods=['GET'])
def return_madlibs_json():
    json = curate_madlibs()
    json['status'] = 'success'
    json['message'] = 'MadLibs story template'
    return json


@app.route("/api/test", methods=['GET'])
def test_flask():
    return {'status': 'success', 'message': 'test'}


if __name__ == '__main__':
    app.run(port=5328)
    