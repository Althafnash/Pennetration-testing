import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800))

targethost = str(input("Enter the host name: "))
targetport = int(input("Enter Port: "))
s.connect((targethost,targetport))

def garb(s):
    try:
        s.send('GET HTTP/1.1 \r\n')
        ret = s.recv(1024)
        print ('[+]' + str(ret))
        return
    except Exception as error:
        print(f"Error {error}")
        return