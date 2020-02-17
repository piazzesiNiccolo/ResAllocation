from network import Node, Device, Network
import marriages as mg
import utils
#crea nodi
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
#crea dispositivi
d1 = Device('1',6)
d2 = Device('2',6)
d3 = Device('3',7)
d4 = Device('4',8)
d5 = Device('5',2)

nx = Network([a,b,c,d,e])
#crea rete con topologia a maglia
nx.set_edges({(a,b),(a,c),(a,d),(a,e),(b,c),(b,d),(b,e),(c,d),(c,e),(d,e)})
#posiziona ogni dispositivo specificando i vicini
d1.position_device([a,c])
d2.position_device([b,d])
d3.position_device([e])
d4.position_device([d,a])
d5.position_device([e,c])
#assegna ciascun dispositivo a un nodo
match = mg.stable_marriage([a,b,c,d,e],[d1,d2,d3,d4,d5])
print(match)
print(d1.ranked_nodes)

