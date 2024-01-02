from vidstream import ScreenShareClient
import threading 

sender= ScreenShareClient('192.168.56.1', 9999) # same computer otherwise specify public ip address here

t= threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
