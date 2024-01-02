from vidstream import ScreenShareClient
import threading 

sender= ScreenShareClient('172.20.10.3', 9999) #same computer

t= threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
