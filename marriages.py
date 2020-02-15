def stable_marriage(nodes, devices):

    while any(node.device == None for node in nodes):
        for d in devices:
            while d.ranked_nodes[0].matched == True:
                d.ranked_nodes.pop(0)
            d.propose_to(d.ranked_nodes[0])

        for node in nodes:
            if len(node.proposals) != 0:
                node.choose_device()
                devices.remove(node.device)
    return sorted(set((node, node.device) for node in nodes), key=lambda x: x[0].name)
