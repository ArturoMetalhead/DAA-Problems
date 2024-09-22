class Node:
    def __init__(self, id: int):
        self.id = id
        self.edges = []
        self.neighbors = []

    def __repr__(self):
        return f"{self.id}"

    def __str__(self):
        return f"{self.id}"
        
    def connect(self, dest: 'Node'):
        e = Edge(self, dest)
        self.edges.append(e)
        self.neighbors.append(dest.id)
        dest.edges.append(e)  # Conexión bidireccional
        dest.neighbors.append(self.id)

class Edge:
    def __init__(self, source: 'Node', dest: 'Node'):
        self.source = source
        self.dest = dest
        self.pheromone = 1.0  # Inicializa las feromonas en la arista
