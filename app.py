from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import main
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def reply():
    data = request.get_json()
    response = main.reply(data['menssagem'])
    return jsonify({"response": response})

app.run()