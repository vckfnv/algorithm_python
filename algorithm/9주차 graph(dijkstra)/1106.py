def dijkstra(start, size, weight):
    # Step 1: initialize distance and visited array
    distance = weight[start] 
    visited = [False] * size
    visited[start] = True # mark start vertex as being visited

    # Step 2: repeat loop until all vertices are visited
    # Step 3: check each vertex for having shortest path
    # Step 4: for each vertex not in visited array, update its shortest path
    
    # Write your code
    
    while visited != [True] * size:
        right = []
        for i in range(size):
            if visited[i] == False:
                right.append(i)
        #print(right)
        for k in right:
            if distance[start]+weight[start][k]<distance[k]:
                distance[k] = distance[start]+weight[start][k]
            
        #print(distance)
        aa = 0
        minval = 1000
        for j in right:
            if distance[j]< minval:
                minval = distance[j]
                aa = j
        #        print(minval, ' ', aa)
                
        visited[aa] = True
        #print(distance)
        #print(visited)
        start = aa
    
            
    
    return distance

def main():
    size = 6

    weight = [
            [0, 2, 5, 1, float('inf'), float('inf')],
            [2, 0, 3, 2, float('inf'), float('inf')],
            [5, 3, 0, 3, 1, 5],
            [1, 2, 3, 0, 1, float('inf')],
            [float('inf'), float('inf'), 1, 1, 0, 2],
            [float('inf'), float('inf'), 5, float('inf'), 2, 0]
    ]

    for i in range(size):
        distance = dijkstra(i, size, weight)
        print("source = {}".format(i), distance)
    
    """
    source = 0 [0, 2, 3, 1, 2, 4]
    source = 1 [2, 0, 3, 2, 3, 5]
    source = 2 [3, 3, 0, 2, 1, 3]
    source = 3 [1, 2, 2, 0, 1, 3]
    source = 4 [2, 3, 1, 1, 0, 2]
    source = 5 [4, 5, 3, 3, 2, 0]
    """

main()
