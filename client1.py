import socket
import threading
import time




PORT = 5050
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
    
    while connected:
     try:
          recvmsg= client.recv(1024).decode(FORMAT)
      
          print(recvmsg)
     except:
        if connected:
          print("problem in getting messages")
        else:
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
        client.close()

        break
     if msg.startswith("/color"):
        if msg[7:14]=="magenta":
            send("\u001b[35m" + msg[15:]+"\u001b[0m")
        if msg[7:12]=="black":
            send("\u001b[30m" + msg[13:]+"\u001b[0m")
        if msg[7:10]=="red":
            send("\u001b[31m" + msg[11:]+"\u001b[0m")
        if msg[7:12]=="green":
            send("\u001b[32m" + msg[13:]+"\u001b[0m")
        if msg[7:11]=="blue":
            send("\u001b[34m" + msg[12:]+"\u001b[0m")
        if msg[7:11]=="cyan":
            send("\u001b[36m" + msg[12:]+"\u001b[0m")
        if msg[7:12]=="white":
            send("\u001b[37m" + msg[13:]+"\u001b[0m")
        if msg[7:13]=="yellow":
            send("\u001b[33m" + msg[14:]+"\u001b[0m")
        else:
            print("unidentified color")
        
     else:
        send(msg)
