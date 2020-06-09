from yeelight import Bulb
import src.utils as utils
import src.CronJob as cron

# todos os metodos utilizam da "classe" utils para o processamento e conversão dos ips do front para a lib da yeelight

# pegar estado atual da lampada especificada por parâmetro 
def getProperties(bulb):
    return bulb.get_properties(requested_properties=[
        "power", "bright", "rgb", "color_mode", "flow", "name", "ct", ])

# metodo a ser executado ao inicializar euma página web para ser a primeira rota do estado atual da lampada
def getStatus(req):
    bulbs, _, _ = utils.getIp(req)
    for i in bulbs:
        if(i != ''):
            return getProperties(i)

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
    
    bulbs, _, _ = utils.getIp(req)

    r = int(req.json.get('r'))
    g = int(req.json.get('g'))
    b = int(req.json.get('b'))

    for bulb in bulbs:
        bulb.set_rgb(r, g, b)
        # bulb.set_color_temp(6700)
        # if r and g and b == 255:
        #     bulb.set_color_temp(6700)


def bandtecColor(req):
    bulbs, _, _ = utils.getIp(req)
    idEnv = 0
    nameEnv = ''
    a = 0

    status = getProperties(bulbs[0])

    bulbs[0].set_rgb(240, 10, 60)
    bulbs[1].set_rgb(239, 182, 97)
    bulbs[2].set_rgb(0, 131, 183)

    for bulb in bulbs:
        try:
            bulb.turn_on()
            a += 1
        except:
            pass

    cron.enable(a, idEnv, nameEnv, status['bright'])


def flow(req):

    bulbs, _, _ = utils.getIp(req)

    for bulb in bulbs:
        bulb.set_color(255, 255, 255)
        print('foi')
        # cron.edit(len(front), idEnv, nameEnv, 1)
