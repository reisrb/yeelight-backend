from yeelight import *
import src.utils as utils
import src.CronJob as cron

# todos os metodos utilizam da "classe" utils para o processamento e conversão dos ips do front para a lib da yeelight

# pegar estado atual da lampada especificada por parâmetro
def getProperties(bulb):
    return bulb.get_properties(requested_properties=[
        "power", "bright", "rgb", "color_mode", "flow", "name", "ct", ])

# metodo a ser executado ao inicializar euma página web para ser a primeira rota do estado atual da lampada
def getStatus(req):
    bulbs = utils.getIp(req)
    print(bulbs)
    return getProperties(bulbs[0])

# Aqui temos dois metodos iguais (turnOn e turnOff) com especificação para esquema de toggle não confudir o usuário
# e ele desligar o front e a lampada ligar "do nada"
def turnOn(req):
    # desestruturando o retorno em var's independentes
    bulbs, nameEnv, idEnv = utils.getIp(req)

    print(bulbs)

    for bulb in bulbs:
        bulb.turn_on()

    # pegando estado atual da lampada referência que ligou com êxito
    bulbsOn = getProperties(bulbs[0])

    # ativando cron para a gravação de logs
    cron.enable(len(bulbs), idEnv, nameEnv, bulbsOn['bright'])
    return f'ligou {bulbs}'

def turnOff(req):
    bulbs, nameEnv, idEnv = utils.getIp(req)

    print(bulbs)
    for bulb in bulbs:
        bulb.turn_off()

    bulbsOn = getProperties(bulbs[0])

    cron.disable(len(bulbs), idEnv, nameEnv, bulbsOn['bright'])
    return f'desligou {bulbs}'

# setar brilho repetindo basicamente o mesmo processo
def setBright(req):
    bright = req.json.get('brilho')
    bulbs, nameEnv, idEnv = utils.getIp(req)

    for bulb in bulbs:
        bulb.set_brightness(int(bright))
        bulbsStatus = getProperties(bulb)

    cron.edit(len(bulbs), idEnv, nameEnv, bulbsStatus['bright'])
    return f"Brilho alterado de {bulbs} lampadas para {bulbsStatus['bright']}"

def setColor(req):
    bulbs = utils.getIp(req)

    r = int(req.json.get('r'))
    g = int(req.json.get('g'))
    b = int(req.json.get('b'))

    for bulb in bulbs:
        bulb.set_rgb(r, g, b)
        if r and g and b == 255:
            bulb.set_color_temp(6491)

def bandtecColor(req):
    bulbs = utils.getIp(req)

    transitions = [
        RGBTransition(7, 98, 200, duration=4500),
        RGBTransition(99, 177, 188, duration=4500),
        RGBTransition(237, 20, 91, duration=4500),
        RGBTransition(239, 182, 97, duration=4500),
    ]

    flow = Flow(
        count=0,
        action=Flow.actions.recover,
        transitions=transitions
    )

    for bulb in bulbs:
        bulb.start_flow(flow)

def flow(req):
    transitions = [
        HSVTransition(hue, 100, duration=500)
        for hue in range(0, 359, 40)]

    flow = Flow(
        count=0,
        transitions=transitions
    )

    bulbs = utils.getIp(req)

    for bulb in bulbs:
        bulb.start_flow(flow)
