import psutil
from os import system, name
from time import sleep
import datetime
import csv

date = datetime.datetime.today().strftime('%Y-%m-%d')
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
dict_list = []
while True:
    traffic = psutil.net_io_counters().bytes_sent / 1000000 + psutil.net_io_counters().bytes_recv / 1000000
    if old_traffic != traffic:
        old_traffic = traffic
        clear()
    print("Today usage: {0:.2f}".format(old_traffic))
        
        # with open('DB.csv', 'r') as outfile:
        #     reader = csv.DictReader(outfile)
    reader = csv.DictReader(open('DB.csv', 'r'))
    for line in reader:
        dict_list.append(line)
            # with open('DB.csv', 'w') as infile:
            #     writer = csv.DictWriter(infile, fieldnames = fieldnames)
            #     data["date"] = date
            #     data["traffic"] = old_traffic
            #     # writer.writeheader()
            #     writer.writerow(data)

    print(dict_list)

    if old_traffic > MAX_USAGE:
        print('Today you spend more than {0:.2f} MegaBytes!'.format(old_traffic))
    sleep(5)
