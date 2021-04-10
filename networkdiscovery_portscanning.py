from socket import *
from icmplib import ping
import ipaddress
import time
import netifaces
startTime = time.time()

# ports to check if open
common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

# Creating a logfile.txt to write the output
f = open("logfile.txt", "w")

# Getting the active Name and IP address of my computer
hostname = gethostname()   
IPAddr = gethostbyname(hostname)   
print("Your Computer Name is:", hostname)
f.write("Your Computer Name is:" + str(hostname) + '\n')
print("Your Computer IP Address is:", IPAddr)
f.write("Your Computer IP Address is:" + str(IPAddr) + '\n')

# Finding the subnet mask using netifaces and read the subnet mask
for iface in netifaces.interfaces():
    iface_details = netifaces.ifaddresses(iface)
    if netifaces.AF_INET in iface_details:
        if ((iface_details[netifaces.AF_INET][0]['addr']) == '192.168.18.19'):
            subnet = iface_details[netifaces.AF_INET][0]['netmask']

# Printing Subnet Mask
print("Your Computer Subnet Mask is:", subnet)
f.write("Your Computer Subnet Mask is:" + str(subnet) + '\n')

# Concatinating the subnet mask with the ip address
#subnet = '255.255.255.0'
IP_Net = IPAddr + '/' + subnet

# Creating an ipAddress object 
net = ipaddress.ip_network(IP_Net, strict = False)

# Finding the active ipaddresses
alive_address = [] # This list will contain all the active ip address in the network

# Scanning through all 'usable' addresses i.e. host addresses
print('\nScanning live ip addresses...')
f.write('\nScanning live ip addresses...\n')
print('\nLive IP Addresses:\n')
f.write('\nLive IP Addresses:\n\n')

count = 0
iterator = 1
check_first_x_hosts = 50     # Change this variable if you need to change the number of hosts
for x in net.hosts():
    if count > check_first_x_hosts:        # Checking for first 50 hosts
        break
    host = ping(str(x))                    # Ping the host 
    count = count + 1
    if(host.is_alive):                     # Check if the host is alive
        alive_address.append(str(x))
        print(str(iterator) + ') ' + str(x))
        f.write(str(iterator) + ') ' + str(x) + '\n')
        iterator = iterator + 1
print('------------------')
f.write('------------------\n')

# Checking the ports of every live ip address and tells which ports are open
for t_IP in alive_address: # Iterating through all the live addresses
    print ('\nStarting scan on host: ', t_IP)
    f.write('\nStarting scan on host: ' + str(t_IP) + '\n')
    open_count = 0
    for i in common_ports: # Check for all ports declared above if they are open or not
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
         f.write('Port ' + str(i) + ': OPEN\n')
         open_count = open_count + 1
    if(not open_count):
        print('No open Port found on this address')
        f.write('No open Port found on this address\n')
        s.close()

# Total time taken for the code to execute
print('\nTime taken:', time.time() - startTime, 'seconds')
f.write('\nTime taken: ' + str(time.time() - startTime) + ' seconds')

# closing the file
f.close()
