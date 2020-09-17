class Graph(object):
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        # Insert an edge (v1, v2) into graph
        """
        Input  >> v1: int, v2: int
        Output >> None
        """

        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        # Delete an edge (v1, v2) in graph
        """
        Input  >> v1: int, v2: int
        Output >> None
        """

        if self.adj_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def contains_edge(self, v1, v2):
        # Return true if an edge (v1, v2) is adjacent and return false if it isn't
        """
        Input  >> v1: int, v2: int
        Output >> None
        """

        return True if self.adj_matrix[v1][v2] > 0 else False

    def __len__(self):
        # Return the size of the graph
        """
        Input  >> None
        Output >> int
        """

        return self.size

    def find_degree(self, vertex):
        # Return the degree of the given vertex
        """
        Input  >> vertex: int
        Output >> int
        """
        count = 0
        for i in range(self.size):
            if self.adj_matrix[vertex][i] == 1:
                count +=1
        return count
        
        

    def display(self):
        # Print the graph
        """
        Input  >> None
        Output >> None
        """
        for i in range(self.size):
            for j in range(self.size):
                print(self.adj_matrix[i][j],end=' ')
            print()


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.display()
    vertex = 3
    print()
    print("Degree of " + str(vertex))
    print(g.find_degree(vertex))


main()
