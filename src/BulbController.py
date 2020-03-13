from yeelight import Bulb

import src.utils as utils
import src.CronJob as cron
import time

environments=[{"id": 1,"nome":"Biblioteca", "lados": [{"id":100,"nome": "FRENTE", "ips": ['10.3.0.21']},{"id":0,"nome": "TUDO", "ips":['10.3.0.21', '10.3.0.22']},{"id":200,"nome": "TRAS", "ips": ['10.3.0.22']}]},{"id": 2,"nome":"1B", "lados": [{"id":100, "nome": "FRENTE", "ips": ['10.3.0.23']},{"id":200, "nome": "TRAS", "ips": ['10.3.0.23']}]},{"id": 0,"nome":"TUDOTUDO", "lados": [{"id":0, "nome": "TUDO", "ips": ['10.3.0.21', '10.3.0.22', '10.3.0.23']}]}]
bulbs = []

def getEnv():
    return environments

def start():
    for value in environments:
        for key in value.get('lados'): 
            for ip in key.get('ips'):
                try:
                    bulbs.append(Bulb(ip, effect="smooth")) 
                except Exception as e:
                    print(e)

def getProperties(bulb):
    return bulb.get_properties(requested_properties=[
                          "power", "bright", "rgb", "color_mode", "flow", "name","ct",])

def getStatus(req):
    listBulbs, _, _ = utils.getSide(req, environments, bulbs)

    return getProperties(listBulbs[0])

def turnOn(req):
    listBulbs, idEnv, nameEnv = utils.getSide(req, environments, bulbs)
    status = getProperties(listBulbs[0])

    for bulb in listBulbs:
        try:
            bulb.turn_on()
        except :
            pass

    cron.enable(len(listBulbs), idEnv, nameEnv, status['bright'])

    return status

def turnOff(req):
    listBulbs, idEnv, nameEnv = utils.getSide(req, environments, bulbs)    
    status = getProperties(listBulbs[0])

    for bulb in listBulbs:
        try:
            bulb.turn_off()
        except :
            pass
        

    cron.disable(len(listBulbs), idEnv, nameEnv, status['bright'])

    return status

def setBright(req):
    bright = req.json.get('brilho')
    
    listBulbs, idEnv, nameEnv = utils.getSide(req, environments, bulbs)    
    status = getProperties(listBulbs[0])

    for bulb in listBulbs:
        time.sleep(1)
        bulb.set_brightness(int(bright))

    cron.edit(len(listBulbs), idEnv, nameEnv, status['bright'])

    return status

def setColor(req):
    listBulbs, _, _ = utils.getSide(req, environments, bulbs)

    r = req.json.get('r')
    g = req.json.get('g')
    b = req.json.get('b')
    
    for bulb in listBulbs:
        bulb.set_rgb(r, g, b)


def bandtecColor(req):
    listBulbs, _, _ = utils.getSide(req, environments, bulbs)
    idEnv = 0
    nameEnv = 'TUDOTUDO'

    status = getProperties(listBulbs[0])
    
    listBulbs[0].set_rgb(240, 10, 60)
    listBulbs[1].set_rgb(239, 182, 97)
    listBulbs[2].set_rgb(0, 131, 183)

    for bulb in listBulbs:
        bulb.turn_on()

    cron.enable(len(listBulbs), idEnv, nameEnv, status['bright'])


def projetor(req):

    front, back, idEnv, nameEnv = utils.setSides(req, environments, bulbs)

    for bulb in front:
        bulb.set_brightness(1)
        cron.edit(len(front), idEnv, nameEnv, 1)

    for bulb in back:
        bulb.set_brightness(40)
        cron.edit(len(back), idEnv, nameEnv, 40)
