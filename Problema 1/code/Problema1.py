import copy
import math
import heapq

class Graph:
    def __init__(self, n, m, edges):
        self.graph = [[] for _ in range(n)]
        self.edges = []
        for u, v, w in edges:
            self.edges.append((u,v,w))
            self.graph[u].append((v,w))
            self.graph[v].append((u,w))

#region First Solution (brute force)

def first_solution(n, m, edges, roads):
    G = Graph(n, m, edges)
    useful_edges = set()

    for road in roads:
        u, v, l = road
        useful_edges_in_road = set()
        paths = []
        get_paths( u, v, l, G, 0,  [], paths)

        for path in paths:
            for edge in path:
                useful_edges_in_road.add(edge)

        useful_edges = useful_edges.union(useful_edges_in_road)

    return len(useful_edges)

def get_paths( u, v, l, G, cost, current_path, total_paths):
    if cost > l:
        return
    
    if u == v and cost <= 1:
        current_path1 = current_path[:]
        #current_path1 = copy.deepcopy(current_path)
        total_paths.append(current_path1)

    for node_ady in G.graph[u]:
        node, c = node_ady
        if cost + c <= 1:
            cost += c
            current_path.append((u, node))
            get_paths(node, v, l, G, cost, current_path, total_paths)
            cost -= c
            current_path.pop()

#endregion

#region Second solution (Dijkstra)

def second_solution(n, m, edges, roads):
    # se crea el grafo
    G = Graph(n, m, edges)

    # calculando 2q Dijkstras
    dist = [None] * n
    for u,v,l in roads:
        if dist[u] is None:
            dist[u] = dijkstra( G, u, n, m)
        if dist[v] is None:
            dist[v] = dijkstra( G, v, n, m)

    # comprobando aristas útiles
    usefull_edges = 0     
    for x,y,w in edges:
        for u,v,l in roads:
            if dist[u][x] + dist[v][y] + w <=l or dist[u][y] + dist[v][x] + w <=l:
                usefull_edges += 1
                break
            
    return usefull_edges

def dijkstra( G, start, n, m):

    distances = [math.inf for _ in range(n)]
    distances[start] = 0

    if m * math.log(n) < n*n:
        return dijkstra_pq( G, start, distances)
    
    return dijkstra_normal(G, n, distances)

def dijkstra_pq( G, start, distances):
    heap = [(0, start)]

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)
        
        # Si el nodo actual ya se actualizo, lo salto
        if current_distance > distances[current_node]:
            continue
        
        # Actualiza la distancia de los nodos adyacentes si es mas corta que la distancia actual
        for node_ady, weight in G.graph[current_node]:
            distance = current_distance + weight
            if distance < distances[node_ady]:
                distances[node_ady] = distance
                heapq.heappush(heap, (distance, node_ady))
    
    return distances
    
def dijkstra_normal(G, n, distances):

    visited = [False] * n
        
    for _ in range(n):        
        min_dist = math.inf
        min_node = None
        for node in range(n):
            if not visited[node] and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node        
        if min_node is None:
            break        
        visited[min_node] = True
                
        for node_ady, weight in G.graph[min_node]:            
            if weight > 0 and not visited[node_ady]:
                distance = distances[min_node] + weight
                if distance < distances[node_ady]:
                    distances[node_ady] = distance    
    return distances

#endregion

#region Third Solution (Dijkstra and Floy-Warshall)

def FloydWarshall(n,edges):
    # Inicializar matriz de distancias
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for (u,v,w) in edges:
        dist[u][v] = dist[v][u] = w

    # Computar camino de costo minimo para todo par de vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])                

    return dist

def third_solution(n, m, edges, roads):
    G = Graph(n, m, edges)
    
    # Primera Parte (calculando los costos mínimos de nodo a nodo)
    d = FloydWarshall(n, edges)

    # Segunda Parte (comprobando aristas útiles)
    usefull_edge_count = 0
    usefull_edges_mark = [[False] * n for _ in range(n)]

    mark = [False] * n
    
    for _ in range(n):
        v = None
        dist = [math.inf] * n
        # Fijando el primer nodo de las triplas
        for vi, ui, li in roads:
            if v == None:
                if not mark[vi]:
                    v = vi
                    mark[v] = True
            if v == vi:
                dist[ui] = - li

        if v == None: break

        dist = dijkstra_normal(G, n, dist)

        for x,y,w in edges:
            if not usefull_edges_mark[x][y]:
                if dist[x] <= -w - d[v][y] or dist[y] <= -w - d[v][x]:
                    usefull_edge_count +=1
                    usefull_edges_mark[x][y] = True
                    usefull_edges_mark[y][x] = True

    return usefull_edge_count

#endregion