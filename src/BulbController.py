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
    print(bulbs[0])
    return getProperties(bulbs[0])


# Aqui temos dois metodos iguais (turnOn e turnOff) com especificação para esquema de toggle não confudir o usuário
# e ele desligar o front e a lampada ligar "do nada"
def turnOn(req):
    ba = 0
    bna = ""
    bulbStatus = 0

    bulbs, nameEnv, idEnv  = utils.getIp(req) # desestruturando o retorno em var's independentes

    for bulb in bulbs:
        try:
            bulb.turn_on()
            ba += 1
            bulbStatus = bulb # setando na variavel pelo menos a ultima lampada que ligou com êxito
        except :
            bna += f'({bulb})/mac\n'  # setando na variavel lampadas que não ligou com êxito
            pass

    bulbsOn = getProperties(bulbStatus) # pegando estado atual da lampada referência que ligou com êxito
 
    cron.enable(ba, idEnv, nameEnv, bulbsOn['bright']) # ativando cron para a gravação de logs
    return f'ligou {ba} ----- não ligou {bna}'

def turnOff(req):
    ba = 0
    bna = ""
    bulbStatus = 0
    
    bulbs, nameEnv, idEnv = utils.getIp(req)

    for bulb in bulbs:
        try:
            bulb.turn_off()
            ba += 1
            bulbStatus = bulb
        except :
            bna += f'({bulb})/mac\n'
            pass

    bulbsOn = getProperties(bulbStatus)

    cron.disable(ba, idEnv, nameEnv, bulbsOn['bright'])
    return f'desligou {ba} ----- não desligou {bna}'


# setar brilho repetindo basicamente o mesmo processo

def setBright(req):
    ba = 0
    bright = req.json.get('brilho')
    bulbs, nameEnv, idEnv = utils.getIp(req)

    for bulb in bulbs:
        bulb.set_brightness(int(bright))
        bulbsStatus = getProperties(bulb)
        ba += 1

    cron.edit(ba, idEnv, nameEnv, bulbsStatus['bright']) 
    return f"Brilho alterado de {ba} lampadas para {bulbsStatus['bright']}"


def setColor(req):
    bulbs = utils.getIp(req)

    r = int(req.json.get('r'))
    g = int(req.json.get('g'))
    b = int(req.json.get('b'))

    for bulb in bulbs:
        try:
            bulb.set_rgb(r, g, b)
            if r and g and b == 255:
                bulb.set_color_temp(6491)
        except:
            pass


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


