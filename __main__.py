from flask import Flask, request, jsonify
from flask_cors import CORS

import src.BulbController as BulbController
import src.CronRead as CronRead
import time

app = Flask(__name__)
CORS(app)

# rotas da API para especificar qual metodo vai ser executado ao disparar

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


@app.route('/definirCor', methods=['POST'])
def definirCor():
    BulbController.setColor(request)
    return jsonify("Cor alterada")


@app.route('/bandtec', methods=['POST'])
def bandtec():
    BulbController.bandtecColor(request)
    return jsonify("cor bandtec")


@app.route('/setFlow', methods=['POST'])
def projetorSala():
    BulbController.flow(request)
    return jsonify("Projetor ativado")


@app.route('/month', methods=['POST'])
def sumMonth():
    sumM = CronRead.instructions(request)
    return jsonify(sumM)



# bloco para especificar aonde queremos que nosso código seja executado apenas sob condições especiais
if __name__ == "__main__":
    app.run(host='localhost', debug=True)
