import os 

IP = input('Enter the IP Address : ')
print(f'[+] start pinging {IP}')
dot = IP.rfind('.')
IP = IP[0:dot + 1]

for i in range(1,255):
    host = IP = str(i)
    response = os.system(f'ping -c l -w 1 {host} >/dev/null')

    if response == 0:
        print(f'{host} is UP')
    else:
        print(f'{host} is DOWN')
