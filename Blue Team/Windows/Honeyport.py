'''
    For python 2.7.0

    This script listens on a port of your choosing and 
    blacklists IP addresses that try to connect to it
    using advanced firewall.    
'''

import socket

# Config
friendly_server = '192.168.3.120'
bait_port = 445
friendly_port = 5860
friendlies = ['192.168.3.163', '192.168.2.1']

def collect():
    '''
    Listens for hostile connections
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', bait_port))
    sock.listen(1)
    conn, addr = sock.accept()
    print ('Connected by ', addr)
    conn.close()
    report(addr)


def report(att_ip):
    '''
    Sends potentially malicious IP to server
    '''
    # Ignore friendly addresses (vulnerability scans, etc.)
    if att_ip in friendlies:
        return collect()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((friendly_server, friendly_port))
    sock.sendall(att_ip)
    return collect()

    
