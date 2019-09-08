from datetime import datetime
import time

def add_worker(emp,workers=None):
    if workers==None:
        workers=[]
    workers.append(emp)
    return workers

def display_time(time=None):
    if time==None:
        time=datetime.now()
    print(time.strftime('%Y-%m-%d,%H:%M:%S'))

# display_time()
# time.sleep(1)
# display_time()
# time.sleep(10)
# display_time()

# zip() return a generator object

# bad pratice
# from os import *