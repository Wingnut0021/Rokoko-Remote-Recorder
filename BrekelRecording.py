import socket

TCP_IP = "192.168.50.52"
PORT = 8889

#MESSAGE = b"Brekel_recording_start"
BUFFER_SIZE = 1024

#print("UDP target IP:", UDP_IP)
#print("UDP target port:", UDP_PORT)
#print("message:", MESSAGE)



def brekel_start():
    MESSAGE = "Brekel_recording_start"
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((TCP_IP,PORT))
    s.send(bytes(MESSAGE,'UTF-8'))
    #print (s.recv(BUFFER_SIZE))
    #print("Received data:",data)
    s.close()