from Graph import *

def check_clique(nodes: list):
    
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i].id not in nodes[j].neighbors:
                return False
    
    return True