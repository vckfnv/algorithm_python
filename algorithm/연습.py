





































def na(a,b,c):
    K =[[0 for x in range(c+1)] for x in range(len(a)+1)]
    for i in range(len(a)+1):
        for w in range(c+1):
            if i ==0 or w == 0:
                K[i][w] = 0
            elif a[i-1] <= w:
                K[i][w] = max(b[i-1]+K[i-1][w-a[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[len(a)][c]
print(na([2,1,3,2],[12,10,20,15],5))

def lc(x,y):
    m = len(x)
    n = len(y)
    c = [[0 for x in range(n+1)]for x in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                if c[i-1][j]>=c[i][j-1]:
                    c[i][j] = c[i-1][j]
                else:
                    c[i][j] = c[i][j-1]

    return c

print(lc('ABCB','BDCA'))


def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        least = i
        # write your code :)
        find = i
        mini = i
        while find < n:
            if arr[find] < arr[mini]:
                mini = find
            else:
                find += 1
        arr[least], arr[mini] = arr[mini], arr[least]        
        
    return arr

def partition(arr, left, right):
    pivot = arr[left] # make the first element as pivot 
    pivotindex = left
    # write your code :)
    
    l = left
    h = right
    while l < h:
        while l <= h and arr[l] <= pivot:
            l = l+1
        while l <= h and arr[h] >= pivot:
            h = h-1
            
        if l <= h:
            arr[l], arr[h] = arr[h], arr[l]
            l += 1
            h -= 1
    
    arr[pivotindex], arr[h] = arr[h], arr[pivotindex]
    
    return h
# write your code :)
def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p-1) # sorts the left side of pivot 
        quick_sort(arr, p + 1, right) # sort the right side of pivot.

    return arr

def merge_sort(arr):
    n = len(arr)

    if n > 1:
        # find the mid point
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # sort the left and right part
        merge_sort(left)
        merge_sort(right)

        # merge
        # write your code :)
        l = h = k = 0
        while l < len(left) and h < len(right):
            if left[l] < right[h]:
                arr[k] = left[l]
                l += 1
                k += 1
            else:
                arr[k] = right[h]
                h += 1
                k += 1
        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1
        while h < len(right):
            arr[k] = right[h]
            h += 1
            k += 1
        
    return arr

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
