import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'google.com.au'


def port_scan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False

for i in range(1, 1024):
    if port_scan(i):
        print('Port', i, 'is open')
    else:
        print('Port', i, 'is closed')