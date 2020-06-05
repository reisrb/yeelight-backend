from yeelight import Bulb

def getIp(req): #recebendo req como paramentro que seria o ip da sala, nome e ips das lampadas
    bulbs = []

    idEnv = int(req.json.get('idSala'))
    nameEnv = req.json.get('nomeSala')

    for ips in req.json.get('ip'):
        bulbs.append(Bulb(ips, effect="smooth",  duration=100))    

    return (bulbs, idEnv, nameEnv)