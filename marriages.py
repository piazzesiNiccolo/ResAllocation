
def stable_marriage(nodes, devices):
    
    while any(d.matched==False for d in devices):
        for d in devices:
            if not d.matched:
                d.propose_to(d.ranked_nodes[0])

        for node in nodes:
            if len(node.proposals) != 0:
                node.choose_device()
    return list((node, node.device) for node in nodes)
