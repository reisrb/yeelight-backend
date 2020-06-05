from yeelight import Bulb

def getIp(req):
    bulbs = []

    idEnv = int(req.json.get('idSala'))
    nameEnv = req.json.get('nomeSala')

    for ips in req.json.get('ip'):
        bulbs.append(Bulb(ips, effect="smooth",  duration=100))    

    return (bulbs, idEnv, nameEnv)