class GraphNode:
    
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None
        
        
class Graph:

    def __init__(self, size):
        self.adj_list = [None] * size
        self.size = size
        
    def insert_edge(self, u, v):
        ## Insert an edge(u, v) into graph
        """
        Input:  u, v
        Output: print("vertex index error") if input vertex is out of range
        """  
        if u >= self.size or v >= self.size:
            print("vertex index error")
            return
        
        # v -> u
        new_node = GraphNode(v)
        new_node.next = self.adj_list[u]
        
        self.adj_list[u] = new_node

        # u -> v
        new_node = GraphNode(u)
        new_node.next = self.adj_list[v]
        
        self.adj_list[v] = new_node
        
  
    def depth_first_search(self, v, visited=None): 
        # DFS - traverses a graph in a depthward
        """
        Input:  value
        Output: print(v, end = ' ')
        """  
        if visited == None:
            visited = [False] * (self.size) 
        
        visited[v] = True
        print(v, end = ' ') 
  
  
        start_node = self.adj_list[v]
        while start_node:
            if visited[start_node.vertex] == False: 
                self.depth_first_search(start_node.vertex, visited)
            start_node = start_node.next
            
    def breadth_first_search(self, v): 
        # BFS - traverses a graph in a breadthward
        """
        Input:  v
        Output: print(v, end = ' ')
        """

        # init
        visited = [False] * (self.size) 
        queue = [] 
  
        # mark v as visited
        visited[v] = True
        # insert v into a queue Q
        queue.append(v) 
        
        
        while queue: 
            v = queue.pop(0) # Remove the item at the given position in the list, and return it
            print (v, end = " ") 

            start_node = self.adj_list[v]
            
            while start_node:
                if visited[start_node.vertex] == False: 
                    queue.append(start_node.vertex)
                    visited[start_node.vertex] = True
                start_node = start_node.next
        
    def display(self):
        ## Completed Function - Do not remove
        # Display graph adjacency list
        for i in range(self.size):
            if self.adj_list[i] != None:
                print(i, end='')
                
                values = []
                start_node =  self.adj_list[i]
                while start_node:
                    values.append(start_node.vertex)
                    start_node = start_node.next

                print(" ", ' -> '.join(map(str,values)))
            else:
                print(i)
            
        
def main():
    graph = Graph(5)

    graph.insert_edge(0,4)
    graph.insert_edge(0,2)
    graph.insert_edge(0,1)
    graph.insert_edge(2,4)
    graph.insert_edge(2,3)
    graph.insert_edge(3,4)
    
    graph.display()
    print("DFS", end = '\t')
    graph.depth_first_search(0) # 0 1 2 3 4 
    print("\nBFS", end ='\t')
    graph.breadth_first_search(0) # 0 1 2 4 3 
    
main()
