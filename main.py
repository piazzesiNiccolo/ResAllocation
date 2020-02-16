from network import Node, Device, Network
import marriages as mg
import utils
a = Node('a')
b = Node('b')
c = Node('c')
d1 = Device('1',3)
d2 = Device('2',6)
d3 = Device('3',5)
nx = Network([a,b,c])
nx.set_edges({(a,b),(a,c),(b,c)})
d1.position_device([a])
d2.position_device([a])
d3.position_device([a])
match = mg.stable_marriage([a,b,c],[d1,d2,d3])
print(match)

