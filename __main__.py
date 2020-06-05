from flask import Flask, request, jsonify
from flask_cors import CORS

import src.BulbController as BulbController
import time

app = Flask(__name__)
CORS(app)


@app.route('/status', methods=['POST'])
def status():
    response = BulbController.getStatus(request)
    return jsonify(response)


@app.route('/ligar', methods=['POST'])
def ligar():
    situacao = BulbController.turnOn(request)
    return jsonify(situacao)


@app.route('/desligar', methods=['POST'])
def desligar():
    situacao = BulbController.turnOff(request)
    return jsonify(situacao)


@app.route('/definirBrilho', methods=['POST'])
def definirBrilho():
    BulbController.setBright(request)
    return jsonify("Brilho alterado")


@app.route('/setCor', methods=['POST'])
def definirCor():
    BulbController.setColor(request)
    return jsonify("Cor alterada")


@app.route('/bandtec', methods=['POST'])
def bandtec():
    BulbController.bandtecColor(request)
    return jsonify("cor bandtec")


@app.route('/projetorSala', methods=['POST'])
def projetorSala():
    BulbController.projetor(request)
    return jsonify("Projetor ativado")


@app.route('/sumMonth', methods=['GET'])
def sumMonth():
    env = BulbController.environments
    sumM = CronRead.instructions(request, env)
    return jsonify(sumM)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
