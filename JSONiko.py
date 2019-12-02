from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict
from nick_prog_Radio import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Backend"

@app.route("/listar_programacao")
def listar_programacao():
    programacao = list(map(model_to_dict(), Programacao.select()))
    return jsonify ({'lista': programacao2211})

app.run(debug=True, port = 4999)