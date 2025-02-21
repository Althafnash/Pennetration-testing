import socket
import logging
from datetime import datetime 

logging.basicConfig(filename='Hjoneypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_HoneyPot(host='0.0.0.0',port=8080):
    sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sever_socket.bind((host,port))
    sever_socket.listen(5)
    print(f'[+] HoneyPot is running at {host} : {port}')

    while True:
        client_socket ,client_addr = sever_socket.accept()
        print(f'[!] connection from {client_addr}')
        logging.info(f'Connection from {client_addr} at socket {client_socket}')
        client_socket.close()

if __name__ == '__main__':
    start_HoneyPot()

