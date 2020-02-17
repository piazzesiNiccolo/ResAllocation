from network import Node, Device
import random


def create_n_nodes(n: int):
    """ crea n nodi """
    nodes = []
    for i in range(25):
        nodes.append(Node('node'+str(i)))
    return nodes


def create_n_devices_with_random_priority(n: int):
    """ crea lista di n dispositivi con priorità casuale tra 1 e 10 """
    devices = []
    for i in range(n):
        devices.append(Device('device' + str(i), random.randrange(1, 11)))
    return devices
