import psutil
from os import system, name
from time import sleep
import datetime
import csv

DATE = datetime.datetime.today().strftime('%Y-%m-%d')
MAX_USAGE = 1024

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

old_traffic = 0
fieldnames = ['date', 'traffic']
db = []

while True:
    traffic = psutil.net_io_counters().bytes_sent / 1000000 + psutil.net_io_counters().bytes_recv / 1000000
    if old_traffic != traffic:
        old_traffic = traffic
    clear()
    print("Today usage: {0:.2f}".format(old_traffic))
        
    with open('DB.csv', mode = 'r') as outfile:
        reader = csv.DictReader(outfile)
        db = list(reader)
        outfile.close()

    with open('DB.csv', 'w') as infile:
        writer = csv.DictWriter(infile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow({"date": DATE, "traffic": old_traffic})
        infile.close()

    if old_traffic > MAX_USAGE:
        print('Today you spend more than {0:.2f} MegaBytes!'.format(old_traffic))
    sleep(5)
