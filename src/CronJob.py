from crontab import CronTab
import os

path = os.path.dirname(os.path.abspath(__file__))

my_cron = CronTab(user='reis')

def verification(amount, idEnv, name, bright):
    global my_cron 
    my_cron = CronTab(user='reis')

    for job in my_cron:
        if job.comment==idEnv:
            return job

    job = my_cron.new(command=f'/usr/bin/python3 {path}/CronPrint.py {amount} {name} {bright}', comment=idEnv)
    job.minute.every(1)
    return job

def enable(amount, idEnv, name, bright):
    job = verification(amount, str(idEnv), name, bright)
    
    job.enable()
    
    if job.comment=='0':
        for jobs in my_cron:
            if jobs.comment != '0':
                jobs.enable()

    my_cron.write()

def edit(amount, idEnv, name, bright):
    job = verification(amount, str(idEnv), name, bright)
    job.command=f'/usr/bin/python3 {path}/CronPrint.py {amount} {name} {bright}'
    my_cron.write()     


def disable(amount, idEnv, name, bright):
    job = verification(amount, str(idEnv), name, bright)
    job.enable(False)
    
    if job.comment=='0':
        for jobs in my_cron:
            jobs.enable(False)
    my_cron.write()