import queue
class Device:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.ranked_nodes = []

    def propose_to(self, node):
        node.proposals.append(self)

    def position_device(self, neighbors):
        #classifica i nodi in base alla distanza utilizzando visita in ampiezza
        self.ranked_nodes = neighbors
        q= queue.deque(neighbors)
        while q:
            e = q.pop()
            self.ranked_nodes.append(e)
            for n in e.neighbors:
                if n not in self.ranked_nodes:
                    q.append(n)


    def __repr__(self):
        return str(self.name)


class Node:
    def __init__(self, name):
        self.name = name
        self.proposals = []
        self.neighbors = set()
        self.matched = False
        self.device = None

    def add_neighbors(self, neighbors):
        for n in neighbors:
            if n not in self.neighbors and self not in n.neighbors:
                self.neighbors.add(n)
                n.neighbors.add(self)

    def choose_device(self):
        self.proposals.sort(key=lambda x: x.priority, reverse=True)
        self.device = self.proposals.pop(0)
        if len(self.proposals) > 0:
            for p in self.proposals:
                p.ranked_nodes.remove(self)
            self.proposals.clear()
        self.matched = True

    def __repr__(self):
        return str(self.name)


class Network(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = self.set_edges()

    def set_edges(self):
        edges = set()
        for n in self.nodes:
            for ne in n.neighbors:
                edges.add((n, ne))
        return edges

    def get_edges(self):
        return self.edges
