def getSide(req, env, bulbs):
    idEnv = int(req.args.get('idAmbiente'))
    idSide = int(req.args.get('idLado'))
    listBulbs = []
    nameEnv = ''

    for value in env:
        if value.get('id') == idEnv:
            nameEnv = value.get('nome')
            for key in value.get('lados'): 
                if key.get('id') == idSide:
                    for ip in key.get('ips'):
                        for bulb in bulbs:
                            if(bulb._ip == ip):
                                listBulbs.append(bulb)
                                break

    return (listBulbs, idEnv, nameEnv) 

def setSides(req, env, bulbs):
    idEnv = int(req.args.get('idAmbiente'))
    back = []
    front = []
    nameEnv = ''
    
    for value in env:
        if value.get('id') == idEnv:
            nameEnv = value.get('nome')
            for key in value.get('lados'): 
                if key.get('nome') == "FRENTE":
                    for ip in key.get('ips'):
                        for bulb in bulbs:
                            if(bulb._ip == ip):
                                front.append(bulb)
                                break
                elif key.get('nome') == "TRAS":
                    for ip in key.get('ips'):
                        for bulb in bulbs:
                            if(bulb._ip == ip):
                                back.append(bulb)
                                break

    return (front, back, idEnv, nameEnv)