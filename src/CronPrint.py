import datetime
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

amountLamp = int(sys.argv[1])
nameEnv = sys.argv[2]
bright = int(sys.argv[3])
    
x = datetime.datetime.now()
date = f'{x.day:02d}/{x.month:02d}/{x.year}'

with open(f'{path}/../logs/{nameEnv}.txt', 'a') as outFile:
    cost = (amountLamp*0.0028)*(bright/100)
    outFile.write('{} - {:.5f}  \n'.format(date, cost))
