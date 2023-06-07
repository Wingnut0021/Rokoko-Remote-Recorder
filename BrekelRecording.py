import socket
import asyncio

TCP_IP = "127.0.0.1"
TCP_PORT = 8889

#MESSAGE = b"Brekel_recording_start"
BUFFER_SIZE = 1024

#print("UDP target IP:", UDP_IP)
#print("UDP target port:", UDP_PORT)
#print("message:", MESSAGE)



def brekel_start():
    MESSAGE = b"Brekel_recording_start\tTIMESHIFTVIS"
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((TCP_IP,TCP_PORT))
        #s.sendall(MESSAGE)
        data = s.recv(1024)

    print(f"Received {data!r}")



    s.close()
    #print (s.recv(BUFFER_SIZE))
    #print("Received data:",data)
