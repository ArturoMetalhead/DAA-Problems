import random
from Graph import *

class AntColony:
    def __init__(self, nodes: list, k: int, n_ants=10, alpha=1, rho=0.5, iterations=100):
        self.nodes = nodes
        self.k = k  # Tamaño mínimo del clique
        self.n_ants = n_ants  # Número de hormigas
        self.alpha = alpha  # Importancia de las feromonas
        self.rho = rho  # Tasa de evaporación de feromonas
        self.iterations = iterations

    def init_pheromones(self):
        for node in self.nodes:
            for edge in node.edges:
                edge.pheromone = 1.0  # Inicializa las feromonas en todas las aristas

    def pheromone_factor(self, node):
        return sum([1.0 for edge in node.edges])  # Retorna un valor simple para la probabilidad

    def create_clique(self):
        for _ in range(self.n_ants):
            current_clique = []
            visited = set()
            start_node = random.choice(self.nodes)
            current_clique.append(start_node)
            visited.add(start_node.id)

            added_node = True

            while len(current_clique) < self.k and added_node:#
                possible_nodes = [n for n in self.nodes if n.id not in visited]
                if not possible_nodes:
                    break

                pheromone_probs = [self.pheromone_factor(n) for n in possible_nodes]
                total_pheromone = sum(pheromone_probs)
                if total_pheromone == 0:
                    break

                probs = [p / total_pheromone for p in pheromone_probs]
                next_node = random.choices(possible_nodes, weights=probs)[0]

                if all(next_node.id in n.neighbors for n in current_clique):
                    current_clique.append(next_node)
                    visited.add(next_node.id)
                else:
                    added_node = False


            # Si se encuentra un clique de tamaño k o mayor, devolverlo inmediatamente
            if len(current_clique) >= self.k:
                return current_clique

            # Evaporación de feromonas
            for node in current_clique:
                for edge in node.edges:
                    edge.pheromone += 1.0  # Refuerza las feromonas en las aristas del clique encontrado

            # Evaporación de feromonas
            for node in self.nodes:
                for edge in node.edges:
                    edge.pheromone *= (1 - self.rho)

    def solve(self):
        self.init_pheromones()
        
        for _ in range(self.iterations):
            clique_found = self.create_clique()
            if clique_found:  # Si se encontró un clique de tamaño k o mayor
                return len(clique_found), [node for node in clique_found]

        return 0, []  # Si no se encontró ningún clique