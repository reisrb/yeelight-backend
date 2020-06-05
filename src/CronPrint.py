import datetime 
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

amountLamp, nameEnv, bright = (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))

d = datetime.datetime.now()

date = f'{d.strftime("%d")}/{d.strftime("%m")}/{d.strftime("%Y")}'

with open(f'{path}/../logs/{nameEnv}.txt', 'a') as outFile:
    cost = (amountLamp*0.0028)*(bright/100)
    outFile.write(f'{date} - {cost:.5f}  \n')
