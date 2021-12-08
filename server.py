import socket 
import threading



PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECTMESSAGE= 'BYE!3808fuhdh32u'
lcon= []
laddr= []
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    connected = True
    def sendclients(msg):
        for c in lcon:
             try:
               if not c==conn:
                c.send(msg.encode(FORMAT))
             except:
                 pass

    sendclients(f"{addr} has joined the chat")
    print(f"{addr} has joined the chat")
    while connected:
     try:
           msg = conn.recv(1024).decode('utf-8')
           
           if msg == DISCONNECTMESSAGE:
               connected = False
               lcon.remove(conn)
               laddr.remove(addr)
               sendclients(f"{addr} has left the chat")
               print(f"{addr} has left the chat")
               break

           if msg.startswith("/private"):
            
               
               paddr= (msg[9:21], int(msg[23:28]))
              
               index = laddr.index(paddr)
               lcon[index].send(msg[29:].encode(FORMAT))
               
           else:
               sendclients(f'{addr}: {msg}')
               print(f'{addr}: {msg}')
           

     except:
         connected= False

         sendclients(f"{addr} has connection issues or left the chat")
         print(f"{addr} has connection issues or left the chat")
      


def start():
    server.listen()
    while 1:
        conn, addr = server.accept()
        ask=input(f"{addr} wants to join to accept type 'accept' else type 'n' ")
        if ask=='accept':
           yes="you are accepted"
           lcon.append(conn)
           laddr.append(addr)
           thread = threading.Thread(target=handle_client, args=(conn, addr))
           thread.start()
           conn.send(yes.encode(FORMAT))
           print(addr)

           print(f'there are {threading.active_count()-1}')
        else:
            no='qhskdnrjissskfn31729312456'
            conn.send(no.encode(FORMAT))


print("starting........",SERVER)
start()
