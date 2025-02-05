class GraphNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, nodesList, directed:bool):
        self.directed = directed
        self.graph = dict()
        for i in nodesList:
            self.graph[i] = []
            
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        
        if not self.directed:
            self.graph[dest].append(src)
    
    def print_graph(self):
        # adjacency list
        print("ADJACENCY LIST")
        print(self.graph)
    
    def adj_matrix(self):
        print("ADJACENCY MATRIX:")
        for row in self.graph:
            for col in self.graph:
                if col in self.graph[row]: print("1 ", end="")
                else: print("0 ", end="")
            print()
    
    def inci_matrix(self):
        print("INCIDENCE MATRIX")
        nodes = self.graph.keys()
        edges = [(n1, n2) for n1 in nodes for n2 in self.graph[n1]]
        for row in self.graph:
            for col in edges:
                if row == col[0]: print("01 ", end="")
                elif row == col[1]:
                    if self.directed: print("-1 ", end="")
                    else: print("01 ", end="")
                else:
                    print("00 ", end="")
            print()

graph = Graph(range(5), directed=True)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()
graph.adj_matrix()
graph.inci_matrix()