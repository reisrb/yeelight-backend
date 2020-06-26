import os

path = os.path.dirname(os.path.abspath(__file__))

# def instructions(req, env):
def instructions(req):
    nameEnv = req.json.get('nomeSala')
    mes = '05'
    total = 0.0

    try:
        f = open(f'{path}/../logs/{nameEnv}.txt', 'r')
        for line in f:
            try:
                total += float(line.split('-')[1].strip()) 
            except ValueError:
                print(f'{line} is not a number!')
    except:
        pass
            
    return f'{total:.5f}' if total != 0.0 else 'Sem registros'