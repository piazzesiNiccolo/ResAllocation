import queue


class Device:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.ranked_nodes = []
        self.matched = False

    def propose_to(self, node):
        node.proposals.append(self)

    def position_device(self, neighbors):
        # classifica i nodi in base alla distanza utilizzando visita in ampiezza
        self.ranked_nodes = list(neighbors)
        q = queue.deque(neighbors)
        while q:
            e = q.popleft()
            if e not in self.ranked_nodes:
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

    def add_neighbor(self, n):
        if n not in self.neighbors and self not in n.neighbors:
            self.neighbors.add(n)
            n.neighbors.add(self)

    def choose_device(self):
        # associa al nodo il dispositivo che si è proposto con priorità massima
        dev = max(self.proposals, key=lambda x: x.priority)

        if self.device == None:
            self.device = dev
        elif dev.priority > self.device.priority:
            self.device.matched = False
            self.device = dev
        self.device.matched = True
        ##
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
        self.edges = set()

    def set_edges(self, edges=set()):
        self.edges = edges
        for n1, n2 in edges:
            n1.add_neighbor(n2)

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.add(edge)
            edge[0].add_neighbor(edge[1])

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

    def get_edges(self):
        return self.edges
