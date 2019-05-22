import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import main
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def index():
    return "<h1>Hello World</hi>"

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def reply():
    data = request.get_json()
    response = main.reply(data['menssagem'])
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='192.168.0.240', port=port)