from network import Node, Device
import random

##crea n nodi
def create_n_nodes(n: int):
    nodes = []
    for i in range(25):
        nodes.append(Node('node'+str(i)))
    return nodes

#crea lista di n dispositivi con priorità casuale tra 1 e 10
def create_n_devices(n: int):
    devices = []
    for i in range(n):
        devices.append(Device('device' + str(i), random.randrange(1, 11)))
    return devices
