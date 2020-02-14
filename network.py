class Device:
    def __init__(self, name, priority, nodes=None):
        self.name = name
        self.priority = priority
        self.prefs = sorted(nodes, key=distance)

    def propose_to(self, node):
        node.proposals.add(self)

    def __repr__(self):
        return str(self.name)


class Node:
    def __init__(self, name, devices=None):
        self.name = name
        self.proposals = set()
        self.preferences = sorted(devices, key=lambda x: x.priority)
        self.device = None

    def choose_device(self, choice):
        self.device = choice
        self.proposals.remove(choice)
        if len(self.proposals > 0):
            for p in self.proposals:
                p.prefs.remove(self)
            self.proposals.clear()

    def __repr__(self):
        return str(self.name)
