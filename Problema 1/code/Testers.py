from Problema1 import first_solution, second_solution, third_solution
from TestGenerator import generate
import time
from random import randint


algorithm = {"1" : first_solution, "2" : second_solution, "3" : third_solution}

print("1: First Aproximation", "2: Second Aproximation", "3: Third Aproximation")

alg= input("Put the algorithm you want to see \n")

num_cases = int(input("Insert how many cases you want to generate: \n"))

if alg  == "1":
    edges = [
        (0,1,3),
        (0,2,5),
        (1,3,2),
        (2,3,4)
    ]
    roads = [(0,1,4), (0,2,2)]

    print(f"n: {4}, m: {len(edges)}, edges: {edges}, roads: {roads}")
    start_time = time.time()
    print(f"solution: {algorithm[alg](4,len(edges),edges,roads)}")
    end_time = time.time()

else:
    avg_edges = 4
    dev_edges = 2
    avg_useful_paths = 3
    dev_useful_paths = 1
    
    for i in range(num_cases):
        amount_vertex = randint(10,600) # number of vertex to create
        case = generate(amount_vertex, avg_edges, dev_edges, avg_useful_paths, dev_useful_paths)
        
        edges = [] 
        for u,v in case[1]:
            w = case[1][(u,v)]
            edges.append((u-1,v-1,w))
            
        roads=[]
        for u,v,l in case[2]:
            roads.append((u-1,v-1,l))
                
        print(f"n: {case[0]}, m: {len(edges)}, edges: {edges}, roads: {case[2]}")
        start_time = time.time() 
        print(f"solution: {algorithm[alg](case[0],len(case[1]),edges,roads)}")
        end_time = time.time()
        print(f'time case {i}: {end_time - start_time}')

