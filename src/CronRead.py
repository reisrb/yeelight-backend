import os

path = os.path.dirname(os.path.abspath(__file__))

def instructions(req, env):
    nameEnv = req.args.get('nomeAmbiente')

    print(nameEnv)

    total = 0.0

    for value in env:
        if value.get('nome') == nameEnv:
            try:
                with open(f'{path}/../logs/{nameEnv}.txt', 'r') as rFile:
                    for line in rFile:
                        try:
                            total += float(line[13:20]) 
                        except ValueError:
                            print('{} is not a number!'.format(line))
            except:
                pass
            
    return f'{total:.2f}' if total != 0.0 else 'Sem registros'