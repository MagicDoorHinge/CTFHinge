'''
    For python 2.7.0

    This script listens on a port of your choosing and 
    blacklists IP addresses that try to connect to it
    using advanced firewall.    
'''

import socket

port = 445
friendlies = ['192.168.3.163', '192.168.2.1']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()
print ('Connected by ', addr)
option = raw_input("Do you want to blacklist this address? ")