import time
from educs.structure import State

def day():
    return time.gmtime()["tm_mday"]

def hour():
    return time.gmtime()["tm_hour"]

def minute():
    return time.gmtime()["tm_min"]

def millis():
    end_time = time.time_ns()*1000000
    diff = end_time - State.start_time
    return diff

def month():
    return time.gmtime()["tm_mon"]

def second():
    return time.gmtime()["tm_sec"]

def year():
    return time.gmtime()["tm_year"]