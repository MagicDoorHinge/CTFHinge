'''
    This script should be run on your domain controller and configured
    to point at your Honeypot machine
'''
import socket

honeypot_address = '192.168.3.124'
friendly_port = 5860

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', friendly_port))
sock.listen(1)
conn, addr = sock.accept()
while 1:
    att_ip = conn.recv(1024)
    # write firewall blacklist to group policy
    # refresh group policy on remote machines
print("The Honeyport has detected a potentially malicious connection " + 
      f"from {att_ip}")