import psutil
from os import system, name

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

net = psutil.net_io_counters(pernic=True)['Wi-Fi'][1] / 1000000

while 1:
    if net != psutil.net_io_counters(pernic=True)['Wi-Fi'][1] / 1000000:
        net = psutil.net_io_counters(pernic=True)['Wi-Fi'][1] / 1000000
        clear()
        print("Megabytes_recv: {}".format(net))
