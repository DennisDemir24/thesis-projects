import time
import psutil

def startingMeasurement():
    start = time.time()
    getUsage = psutil.cpu_percent()

    return {
        "time": start,
        "usage": getUsage
    }

def endingMeasurement(start):
    end = time.time()
    time = end - start
    cpuUsed = psutil.cpu_percent(start) / 1000
    memUsed = (psutil.virtual_memory() / 1024 / 1024)

    return {
        time,
        cpuUsed,
        memUsed
    }