from network import Node, Device, Network
import marriages as mg
import utils
#crea nodi
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
nodes = [a, b, c, d, e]
#crea dispositivi
d1 = Device('1',6)
d2 = Device('2',3)
d3 = Device('3',7)
d4 = Device('4',8)
d5 = Device('5',2)
devices = [d1, d2, d3, d4, d5]
print('nodi della rete:')
for node in nodes:
    print(node)

print('\n\ndispositivi della rete:')
for dev in devices:
    print(dev)
#crea rete con topologia a maglia
nx = Network([a,b,c,d,e])
nx.set_edges({(a,b),(a,c),(a,d),(a,e),(b,c),(b,d),(b,e),(c,d),(c,e),(d,e)})
#posiziona ogni dispositivo specificando i vicini
d1.position_device([a,c])
d2.position_device([b,d])
d3.position_device([e])
d4.position_device([d,a])
d5.position_device([e,c])
#assegna ciascun dispositivo a un nodo
match = mg.stable_marriage([a,b,c,d,e],[d1,d2,d3,d4,d5])
print('\n\nAssociazioni create:')
for node, device in match:
    print('['+str(node) + ', '+str(device)+']')

