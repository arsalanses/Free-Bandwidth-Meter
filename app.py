import psutil

print("Megabytes_recv: {}".format(psutil.net_io_counters(pernic=True)['Wi-Fi'][1] / 1000000))
