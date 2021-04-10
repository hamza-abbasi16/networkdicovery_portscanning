# networkdicovery_portscanning

# First Part (Network Discovery)

The first part of the code is related to the network discovery, This code will first find the active name and ipaddress of your PC and by using your active ipaddress, this code will find the subnet mask related to this ip address through matching your active address with the other associated network interfaces.

Then this code will find all the possible hosts in your private network and find all the alive IP addresses using ping from icmplib. 

# Second Part (Port Scanning)

The second part of the code will take all the live addresses and scan the popular ports defined (You can change and add) for each and every address inside your network and will give you all the open ports of all the live addresses.

Note: This code will also generate a logfile.txt for all the findings along with printing it on the shell.
