from flask import Flask, jsonify
from flask_restful import Api
app = Flask(__name__)
api = Api(app)

@app.route('/api/v1/health-check')
def getenvironments():
     environments = {
	"name": "RestApi",
        "status": "RUNNING"
     }
     return jsonify(environments)
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8181)
