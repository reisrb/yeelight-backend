from yeelight import Bulb, discover_bulbs
import getmac

def getIp(req): #recebendo req como paramentro que seria o ip da sala, nome e ips das lampadas
    bulbs = []
    nameEnv = req.json.get('idSala')
    idEnv = req.json.get('nomeSala')

    #pegar mac

    # bulbsWlan = []

    # bulbsList = discover_bulbs();

    # for bulb in bulbsList:
    #     ip = bulb['ip']
    #     mac = getmac.get_mac_address(ip=ip)
    #     bulbsWlan.append({"ip": ip, "mac": mac})
    #
    # for mac in req.json.get('mac'):
    #     for bulbLan in bulbsWlan:
    #         if mac == bulbLan['mac']:
    #             bulbs.append(Bulb(bulbLan['ip'], effect="smooth",  duration=100))

    for bulb in req.json.get('ips'):
        bulbs.append(Bulb(bulb, effect="smooth",  duration=100))

    if idEnv != None and nameEnv != None:
        return (bulbs, nameEnv, idEnv)
    else:
        return bulbs

