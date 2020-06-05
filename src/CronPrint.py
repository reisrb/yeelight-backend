from datetime import date
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
# path = os.path.abspath(os.getcwd())

amountLamp = int(sys.argv[1])
nameEnv = sys.argv[2]
bright = int(sys.argv[3])

print(amountLamp, nameEnv, bright)
    
# x = datetime.datetime.now()
date = date.today.strftime("%d/%m/%Y")
# date = f'{x.day:02d}/{x.month:02d}/{x.year}'

with open('{path}/../logs/{nameEnv}.txt'.format(path, nameEnv), 'a') as outFile:
    cost = (amountLamp*0.0028)*(bright/100)
    outFile.write('{} - {:.5f}  \n'.format(date, cost))
