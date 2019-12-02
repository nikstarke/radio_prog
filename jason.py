from flask import Flask, json, jsonify
from flask import request
from nick_prog_Radio import Radio
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return "Backend das rádios:  <a href=/listar_radios> Listar Rádios</a>"


@app.route('/listar_radios')
def listar():
    radio = list(map(model_to_dict, Radio.select()))
    response = jsonify({"lista": radio})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True, port = 4999)