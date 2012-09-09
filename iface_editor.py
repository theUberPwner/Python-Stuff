#######################################################
#The user is able to easily edit their interfaces file
#in linux
#Designed for Ubuntu, not sure about other distros and how
#the config files are constructed. This was created because 
#I was changing my settings a lot and wanted them to be saved
#so I didn't have to change them everytime the computer started
#######################################################

from shutil import copy2
from os import remove

#set the path (Ubuntu/Debian)
file_path = "/etc/network/interfaces"

#get the user input for which interface to edit
#use ifconfig -a to see options
iface_to_edit = str(raw_input("Enter the Interface you wish to change: "))

_address = raw_input("Enter Host IP Address: ")
_network = raw_input("Enter Network Address: ")
_netmask = raw_input("Enter NetMask: ")
_broadcast = raw_input("Enter Broadcast Address: ")
_gateway = raw_input("Enter Gateway IP Address: ")

#create the new file
new_file_path = "/etc/network/new_interfaces"
new_file = open(new_file_path, "w")
with open(file_path, "r") as f:
    lines = f.readlines()
    iface_found = False
    _done = False
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        print line
        if line == "auto " + iface_to_edit and not iface_found:
            iface_found = True
            new_file.write("auto "+iface_to_edit+"\n")
            new_file.write("iface "+iface_to_edit+" inet static"+"\n")
            new_file.write("    address "+str(_address)+"\n")
            new_file.write("    network "+str(_network)+"\n")
            new_file.write("    netmask "+str(_netmask)+"\n")
            new_file.write("    broadcast "+str(_broadcast)+"\n")
            new_file.write("    gateway "+str(_gateway)+"\n")
            continue

        if iface_found:
            if not line.startswith("auto") and not _done:
                done = True
                continue
            
        new_file.write(line+"\n")

    if not iface_found:
        new_file.write("auto "+iface_to_edit+"\n")
        new_file.write("iface "+iface_to_edit+" inet static"+"\n")
        new_file.write("    address "+str(_address)+"\n")
        new_file.write("    network "+str(_network)+"\n")
        new_file.write("    netmask "+str(_netmask)+"\n")
        new_file.write("    broadcast "+str(_broadcast)+"\n")
        new_file.write("    gateway "+str(_gateway)+"\n")

    new_file.close()
    
#replace the old file
copy2(new_file_path,file_path)
remove(new_file_path)
