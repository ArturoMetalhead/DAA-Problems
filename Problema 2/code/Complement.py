from Graph import *

def find_complement(nodes, edges):

    complement_nodes = []
    complement_edges = []

    for node in nodes:
        new_node = Node(node.id)
        complement_nodes.append(new_node)

    for i in range(len(complement_nodes)):
        for j in range(i + 1, len(complement_nodes)):
            v1 = complement_nodes[i]
            v2 = complement_nodes[j]
            e1 = Edge(v1,v2)
            e2 = Edge(v2,v1)
            if nodes[i].id not in nodes[j].neighbors and nodes[j].id not in nodes[1].neighbors:
                complement_edges.append(Edge(v1,v2))
                complement_edges.append(Edge(v2,v1))
                v1.connect(v2)

    return complement_nodes, complement_edges