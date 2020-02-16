def match_maker(nodes,devices = []):
    devices_free = devices[:]
    while devices_free: 
        d = devices_free.pop(0)
        node = d.ranked_nodes[0]
        if not node.matched:
            node.device = d
        else:
            if d.priority > node.device:
                dev = node.device
                node.device = d
                devices_free.append(dev)
            else:
                devices_free.append(d)
    return list((node,node.device) for node in nodes)