from Graph import *
from Ant_Colony import *
from Generator import *
from Brute_Force import *
from Check import *
from Complement import *


def Test1():
    nodes = [Node(i) for i in range(10)]

    edges = set()

    nodes[0].connect(nodes[2])
    nodes[0].connect(nodes[3])
    nodes[0].connect(nodes[5])
    nodes[0].connect(nodes[6])
    nodes[0].connect(nodes[7])
    nodes[0].connect(nodes[8])
    nodes[0].connect(nodes[9])

    nodes[1].connect(nodes[3])
    nodes[1].connect(nodes[7])
    nodes[1].connect(nodes[9])

    nodes[2].connect(nodes[3])
    nodes[2].connect(nodes[7])
    nodes[2].connect(nodes[9])

    nodes[3].connect(nodes[4])
    nodes[3].connect(nodes[5])
    nodes[3].connect(nodes[6])
    nodes[3].connect(nodes[8])
    nodes[3].connect(nodes[9])

    nodes[4].connect(nodes[7])
    nodes[4].connect(nodes[9])

    nodes[5].connect(nodes[7])
    nodes[5].connect(nodes[9])

    nodes[6].connect(nodes[7])
    nodes[6].connect(nodes[9])

    nodes[7].connect(nodes[9])

    for node in nodes:
        for edge in node.edges:
            edges.add(edge)
    
    
    comp_nodes, comp_edges = find_complement(nodes, list(edges))

    # Crear la colonia de hormigas y buscar cliques


    print("Colonia de hormigas")
    ant_colony = AntColony(comp_nodes, k=5, n_ants=10, iterations=100)
    
    clique_size, clique_nodes = ant_colony.solve()
    
    if clique_size > 0:
        print(f"Clique encontrado: Tamaño {clique_size}, Nodos {clique_nodes}")
        print(check_clique(clique_nodes))
    else:
        print("No se encontró ningún clique del tamaño requerido.")

    print("Fuerza bruta")
    clique_nodes = brute_force(comp_nodes, 5)
    if clique_nodes:
        print(f"Clique encontrado: Tamaño 5, Nodos {[n.id for n in clique_nodes]}")
        print(check_clique(clique_nodes))
    else:
        print("No se encontró ningún clique del tamaño requerido.")



def Test2():
    nodes = [Node(i) for i in range(9)]

    nodes[0].connect(nodes[1])
    nodes[0].connect(nodes[3])
    
    nodes[1].connect(nodes[2])
    nodes[1].connect(nodes[4])
    nodes[1].connect(nodes[5])
    
    nodes[2].connect(nodes[3])
    nodes[2].connect(nodes[4])
    nodes[2].connect(nodes[5])
    
    nodes[3].connect(nodes[6])
    
    nodes[4].connect(nodes[5])
    nodes[4].connect(nodes[6])
    nodes[4].connect(nodes[7])

    nodes[5].connect(nodes[8])

    nodes[6].connect(nodes[7])


    edges = set()
    for node in nodes:
        for edge in node.edges:
            edges.add(edge)
    
    
    comp_nodes, comp_edges = find_complement(nodes, list(edges))
    # Crear la colonia de hormigas y buscar cliques

    print("Colonia de hormigas")
    ant_colony = AntColony(comp_nodes, k=4, n_ants=10, iterations=100)
    
    clique_size, clique_nodes = ant_colony.solve()
    
    if clique_size > 0:
        print(f"Clique encontrado: Tamaño {clique_size}, Nodos {clique_nodes}")
        print(check_clique(clique_nodes))
    else:
        print("No se encontró ningún clique del tamaño requerido.")

    print("Fuerza bruta")
    clique_nodes = brute_force(comp_nodes, 4)
    if clique_nodes:
        print(f"Clique encontrado: Tamaño 4, Nodos {[n.id for n in clique_nodes]}")
        print(check_clique(clique_nodes))
    else:
        print("No se encontró ningún clique del tamaño requerido.")



def Generate_and_Test():

    for i in range(10):
        print(f"Test {i+1}")
        nodes = generate_graph(10, 20)

        edges = set()
        for node in nodes:
            for edge in node.edges:
                edges.add(edge)
        
        
        comp_nodes, comp_edges = find_complement(nodes, list(edges))
        k = random.randint(3, 6)

        # Con colonia de hormigas

        print("Colonia de hormigas")

        ant_colony = AntColony(comp_nodes, k, n_ants=10, iterations=100)
        
        clique_size, clique_nodes = ant_colony.solve()
        
        if clique_size > 0:
            print(f"Clique encontrado: Tamaño {clique_size}, Nodos {clique_nodes}")
            print(check_clique(clique_nodes))
        else:
            print("No se encontró ningún clique del tamaño requerido.")

        # Con fuerza bruta

        print("Fuerza bruta")

        clique_nodes = brute_force(comp_nodes, k)
        if clique_nodes:
            print(f"Clique encontrado: Tamaño {k}, Nodos {[n.id for n in clique_nodes]}")
            print(check_clique(clique_nodes))
        else:
            print("No se encontró ningún clique del tamaño requerido.")




def main():
    Test1()
    Test2()
    Generate_and_Test()

if __name__ == "__main__":
    main()
