'''
    For python 2.7.0

    This script listens on a port of your choosing and 
    blacklists IP addresses that try to connect to it
    using advanced firewall.    
'''

import socket

# Config
# friendly_server = '192.168.3.120'
# bait_port = 445
# friendly_port = 5860
friendly_server = '192.168.0.111'
bait_port = 11912
friendly_port = 15357
friendlies = ['192.168.3.163', '192.168.2.1']

'''
Listens for hostile connections
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.0.247', bait_port))
sock.listen(1)
print ("listening on port " + str(bait_port))
conn, addr = sock.accept()
print ('Connected by ' + str(addr))
conn.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((friendly_server, friendly_port))
sock.sendall(addr)
