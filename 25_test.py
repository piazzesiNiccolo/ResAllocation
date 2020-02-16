from network import Node, Device, Network
import utils
import marriages as mg

nodes = utils.create_n_nodes(25)
n_count = len(nodes)
devices = utils.create_n_devices(25)
d_count = len(devices)
nx = Network(nodes)
# crea rete con topologia ad anello
for i in range(len(nodes)):
    edge = (nodes[i], nodes[(i+1) % n_count])
    nx.add_edge(edge)
# posiziona ogni dispositivo tra due nodi consecutivi
for j in range(d_count):
    neigh1 = nodes[j]
    neigh2 = nodes[(j+1) % n_count]
    devices[j].position_device({neigh1, neigh2})
# associa dispositivi ai nodi
print(devices[0].ranked_nodes)
match = mg.stable_marriage(nodes, devices)
print(devices[0].ranked_nodes)
##stampa ogni coppia nodo-dispositivo
for node, device in match:
    print('['+str(node) + ', '+str(device)+']')
