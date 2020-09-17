# -*- coding: utf-8 -*-
"""assign1_flody_student.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VF54v7euhscTOpJmQMeFQ_U8MN4_n4R9
"""

from copy import deepcopy

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[float('inf')] * size for i in range(size)]

    def add_edge(self, i, j, weight):
        self.adj_matrix[i][j] = weight
        
    def floyd(self) :
        # Step 1
        distance = deepcopy(self.adj_matrix) 
        path = [[0] * self.size for i in range(self.size)] 
        for i in range(self.size):
            for j in range(self.size):
                if i != j :
                    path[i][j] = j
        
        # Step 2
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if distance[i][j]> distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k]+distance[k][j]
                        path[i][j] = k
        
        for a in range(self.size):
            for b in range(self.size):
                if self.adj_matrix[a][path[a][b]] == float('inf') or self.adj_matrix[a][path[a][b]] != distance[a][path[a][b]]:
                    path[a][b] = path[a][path[a][b]]
        
            # Step 3
        print("pair\tdistance\tpath")
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    path_i = [i] # path_i will be save the shortest path for vetex i
                    while path_i[-1] != j:
                        path_i.append(path[path_i[-1]][j])
                    print("{i} -> {j}\t{dist}\t{path_list}".format(
                        i = i, j = j, dist = distance[i][j], path_list = ' -> '.join([str(j) for j in path_i])
                    ))

        return distance, path

def main():
    size = 4

    g = Graph(size) # directed_graph
    g.add_edge(1, 0, weight=4)
    g.add_edge(0, 2, weight=-2)
    g.add_edge(1, 2, weight=3)
    g.add_edge(2, 3, weight=2)
    g.add_edge(3, 1, weight=-1)
    
    shortest_path, path = g.floyd()

    """
    pair	distance	path
    0 -> 1	-1	0 -> 2 -> 3 -> 1
    0 -> 2	-2	0 -> 2
    0 -> 3	0	0 -> 2 -> 3
    1 -> 0	4	1 -> 0
    1 -> 2	2	1 -> 0 -> 2
    1 -> 3	4	1 -> 0 -> 2 -> 3
    2 -> 0	5	2 -> 3 -> 1 -> 0
    2 -> 1	1	2 -> 3 -> 1
    2 -> 3	2	2 -> 3
    3 -> 0	3	3 -> 1 -> 0
    3 -> 1	-1	3 -> 1
    3 -> 2	1	3 -> 1 -> 0 -> 2
    """
    

main()
