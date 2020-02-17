import copy

def stable_marriage(nodes, devices):
    
    if len(nodes) != len(devices):
        raise ValueError('Deve esserci lo stesso numero di nodi e dispositivi')
    #copia le liste dei nodi di ciascun dispositivo
    copy_nodes = []
    for d in devices:
        copy_nodes.append(copy.copy(d.ranked_nodes))
    
    while any(d.matched==False for d in devices):
        for d in devices:
            if not d.matched:
                d.propose()

        for node in nodes:
            if len(node.proposals) != 0:
                node.choose_device()
    
    
    for i in range(len(devices)):
        devices[i].ranked_nodes = copy_nodes[i]
    return list((node, node.device) for node in nodes)
