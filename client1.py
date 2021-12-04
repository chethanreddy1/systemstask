import socket
import threading




PORT = 5050
HEADER= 64
FORMAT = 'utf-8'
DISCONNECTMESSAGE = 'BYE!3808fuhdh32u'
SERVER = '192.168.56.1'
ADDR= (SERVER, PORT)
connected=True
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    try:
     client.send(message)
    except:
        print("server problems")

def recive():
    while 1:
     try:
      
          print(client.recv(1024).decode(FORMAT))
     except:
         pass
rejected = client.recv(1024).decode(FORMAT)=='qhskdnrjissskfn31729312456'
if rejected:
    print("admin rejected you")
else:
 print("admin accepted you")
 thread = threading.Thread(target=recive)
 thread.start()


 while connected:

    msg= input()
    
    if msg.startswith("/leave"):
        send(DISCONNECTMESSAGE)
        print("disconnected")
        connected = False
    else:
        send(msg)
