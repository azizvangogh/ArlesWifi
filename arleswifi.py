#cd /etc/NetworkManager/system-connections

import subprocess
def samet (avaible_network):
    print("selam")

avaible_network = input("Give me a network path Ex /etc/NetworkManager/system-connections : ")

samet(avaible_network)

#subprocess.call(["cd", "/etc/NetworkManager/system-connections"])
subprocess.call(["sudo","cat", avaible_network])