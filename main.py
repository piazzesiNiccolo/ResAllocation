from network import Node, Device, Network
import marriages as mg
import utils
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

n1 = Device('1', 2)
n2 = Device('2', 9)
n3 = Device('3', 3)
n4 = Device('4', 10)
n5 = Device('5', 6)
n6 = Device('6', 1)
nodes = [a, b, c, d, e, f]
Net = Network(nodes)
Net.set_edges(
    {(b, c), (a, b),
     (a, d), (e, a),  
     (c, d), (f, d), 
     (b, f)
     })
print(Net.get_edges())
devices = [n1, n2, n3, n4, n5, n6]
n1.position_device([b,c])
n2.position_device([a,f])
n3.position_device([e,d,f])
n4.position_device([c,d])
n5.position_device([e])
n6.position_device([b,c,a,d])
hh = mg.stable_marriage(nodes,devices)
h2 = mg.match_maker(nodes,devices)
print(hh)
print(h2)


