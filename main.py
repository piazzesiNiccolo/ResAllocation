from network import Node, Device

a = Node('a')
b = Node('b')
c = Node('c')
d = Device('d', 2, {b, a, c})
e = Device('e', 4, {b, c, a})
f = Device('f', 8, {a, b, c})
devices = {d, e, f}
nodes = {a, b, c}

sorted(devices, key=lambda x: x.priority)