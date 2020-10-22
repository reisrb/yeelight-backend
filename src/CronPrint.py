import datetime 
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

# amountLamp, nameEnv, bright = (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
amountLamp, nameEnv, bright = (2, 'SALA_1B', 20)
cost = (amountLamp*0.0028)*(bright/100)

d = datetime.datetime.now()
date = f'{d.strftime("%d")}/{d.strftime("%m")}/{d.strftime("%Y")}'

with open(f'{path}/../logs/{nameEnv}.txt', 'a') as outFile:
    outFile.write(f'{date} - {cost:.5f}  \n')
