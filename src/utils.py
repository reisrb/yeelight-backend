from yeelight import Bulb, discover_bulbs

def getIp(req): #recebendo req como paramentro que seria o ip da sala, nome e ips das lampadas
    bulbs = []
    idEnv = req.json.get('idSala')
    nameEnv = req.json.get('nomeSala')

    bulbsList = discover_bulbs()

    print(idEnv, nameEnv, req.json.get('ips'))

    ipEstatico = ['192.168.255.7']

    # for bulb in ipEstatico:
    # for bulb in req.json.get('ips'):
    for bulb in ipEstatico:
        for bulbWlan in bulbsList:
            if bulb == bulbWlan['ip']:
                bulbs.append(Bulb(bulb, effect="smooth",  duration=100))
            else:
                print('Nao ligou', bulbWlan['ip'])

    if idEnv != None and nameEnv != None:
        return (bulbs, nameEnv, idEnv)
    else:
        return bulbs


# import getmac

# def getMac(req): #recebendo req como paramentro que seria o ip da sala, nome e ips das lampadas
#     bulbs = []
#     idEnv = req.json.get('idSala')
#     nameEnv = req.json.get('nomeSala')

#     #pegar mac
#     bulbsWlan = []

#     bulbsList = discover_bulbs()

#     for bulb in bulbsList:
#         ip = bulb['ip']
#         mac = getmac.get_mac_address(ip=ip)
#         bulbsWlan.append({"ip": ip, "mac": mac})
    
#     for mac in req.json.get('mac'):
#         for bulbLan in bulbsWlan:
#             if mac == bulbLan['mac']:
#                 bulbs.append(Bulb(bulbLan['ip'], effect="smooth",  duration=100))

#     if idEnv != None and nameEnv != None:
#         return (bulbs, nameEnv, idEnv)
#     else:
#         return bulbs