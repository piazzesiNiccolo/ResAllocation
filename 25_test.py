from network import Node, Device, Network
import utils
import marriages as mg

#crea i nodi
nodes = utils.create_n_nodes(25)
n_count = len(nodes)
#crea i dispositivi
devices = utils.create_n_devices_with_random_priority(25)
d_count = len(devices)
print('nodi della rete:')
for node in nodes:
    print(node)

print('\n\ndispositivi della rete:')
for dev in devices:
    print(dev)
# crea rete con topologia ad anello
nx = Network(nodes)
for i in range(len(nodes)):
    edge = (nodes[i], nodes[(i+1) % n_count])
    nx.add_edge(edge)

# posiziona ogni dispositivo tra due nodi consecutivi
for j in range(d_count):
    neigh1 = nodes[j]
    neigh2 = nodes[(j+1) % n_count]
    devices[j].position_device({neigh1, neigh2})

# associa dispositivi ai nodi
match = mg.stable_marriage(nodes, devices)

##stampa ogni coppia nodo-dispositivo
print('\n\nAssociazioni create:')
for node, device in match:
    print('['+str(node) + ', '+str(device)+']')
