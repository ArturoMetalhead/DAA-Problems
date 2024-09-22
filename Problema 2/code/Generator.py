from Ant_Colony import *
from Graph import *

def generate_graph(n_nodes, n_edges):
    nodes = [Node(i) for i in range(n_nodes)]

    for _ in range(n_edges):
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)
        if node1 != node2 and node2.id not in node1.neighbors and node1.id not in node2.neighbors:
            node1.connect(node2)

    return nodes


def main():
    #random.seed(0)
    n_nodes = 9
    n_edges = 15
    n_ants = 10
    k = 3
    rho = 0.1
    iterations = 100

    nodes = generate_graph(n_nodes, n_edges)
    ac = AntColony(nodes, n_ants, k, rho, iterations)
    ac.solve()


if __name__ == "__main__":
    main()