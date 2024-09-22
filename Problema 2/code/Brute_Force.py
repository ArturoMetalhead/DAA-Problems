from Graph import *


def sort_by_degree(nodes: list):
    return sorted(nodes, key=lambda n: len(n.neighbors), reverse=True)

def brute_force(nodes: list, k: int):
    def find_clique(current_clique, remaining_nodes):
        if len(current_clique) == k:
            return current_clique

        if not remaining_nodes:
            return []

        for i, node in enumerate(remaining_nodes):
            if all(node.id in n.neighbors for n in current_clique):
                new_clique = current_clique + [node]
                result = find_clique(new_clique, remaining_nodes[i+1:])
                if result:
                    return result

        return []

    nodes = sort_by_degree(nodes)
    return find_clique([], nodes)
    