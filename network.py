import queue


class Device:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.ranked_nodes = []
        self.matched = False

    def propose(self):
        """ si propone al nodo preferito"""
        n = self.ranked_nodes.pop(0)
        n.proposals.append(self)

    def position_device(self, neighbors):
        """ classifica i nodi in base alla distanza utilizzando visita in ampiezza,
        partendo dai vicini"""
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
        self.device = None

    def add_neighbor(self, n):
        if n not in self.neighbors and self not in n.neighbors:
            self.neighbors.add(n)
            n.neighbors.add(self)
    
    def remove_neighbor(self, n):
        if n in self.neighbors and self in n.neighbors:
            self.neighbors.remove(n)
            n.neighbors.remove(self)

    def choose_device(self):
        """associa al nodo il dispositivo  con priorità massima tra le proposte """
        dev = max(self.proposals, key=lambda x: x.priority)
        self.proposals.remove(dev)
        #sceglie il dispositivo
        if self.device == None:
            self.device = dev
        elif dev.priority > self.device.priority:
            self.device.matched = False
            self.device = dev
        self.device.matched = True
        #rigetta, se presenti, le altre proposte
        if len(self.proposals) > 0:
           self.proposals.clear()
        

    def __repr__(self):
        return str(self.name)


class Network:
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
            edge[0].remove_neighbor(edge[1])

    def get_edges(self):
        return self.edges
