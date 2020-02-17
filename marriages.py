import copy

def stable_marriage(nodes = [], devices = []):
    """ forma le associazioni sotto forma di tuple(nodo, dispositivo)"""
    if len(nodes) != len(devices):
        raise ValueError('Deve esserci lo stesso numero di nodi e dispositivi!')
    #copia le liste dei nodi di ciascun dispositivo,in modo da evitare side effects
    copy_nodes = []
    for d in devices:
        copy_nodes.append(copy.copy(d.ranked_nodes))
    
    #effettua l'associazione
    while any(d.matched==False for d in devices):
        for d in devices:
            if not d.matched:
                d.propose()

        for node in nodes:
            if len(node.proposals) != 0:
                node.choose_device()
    
    #ripristina le liste di nodi
    for i in range(len(devices)):
        devices[i].ranked_nodes = copy_nodes[i]
    return list((node, node.device) for node in nodes)
