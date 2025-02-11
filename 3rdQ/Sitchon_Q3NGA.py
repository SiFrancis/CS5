# code modified from FA6
from sys import maxsize

# class GraphNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Graph:
    def __init__(self, nodesList, directed=False, distancesOn=False):
        self.directed = directed
        self.graph = dict()
        for i in nodesList:
            self.graph[i] = []
        self.nodes = self.graph.keys()
        # usign distances between edges for Djikstra's algo
        self.distancesOn = distancesOn
        self.distances = dict()
    
    def add_edge(self, src, dest, distance=0):
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)
        if self.distancesOn:
            self.distances[(src, dest)] = distance
            if not self.directed: 
                self.distances[(dest, src)] = distance
    
    def print_graph(self):
        # adjacency list
        print("ADJACENCY LIST")
        print(self.graph)
    
    def adj_matrix(self):
        print("ADJACENCY MATRIX:")
        for row in self.graph:
            if self.distancesOn:
                for col in self.graph:
                    if col in self.graph[row] and (row, col) in self.distances.keys(): 
                        print(f"{self.distances[(row, col)]:02} ", end="")
                    else: print("00 ", end="")
                print()
            else:
                for col in self.graph:
                    if col in self.graph[row]: print("1 ", end="")
                    else: print("0 ", end="")
                print()
    
    def inci_matrix(self):
        print("INCIDENCE MATRIX")
        edges = [(n1, n2) for n1 in self.nodes for n2 in self.graph[n1]]
        for row in self.graph:
            for col in edges:
                if row == col[0]: print("01 ", end="")
                elif row == col[1]:
                    if self.directed: print("-1 ", end="")
                    else: print("01 ", end="")
                else:
                    print("00 ", end="")
            print()
    
    def minDistance(self, dist, sptSet):
        minVal = maxsize
        minIndex = 0
        for n in self.nodes:
            if dist[n] < minVal and sptSet[n] == False:
                minVal = dist[n]
                minIndex = n
        return minIndex
    
    def print_soln(self, dist, src):
        print("Distance from Start Vertex " + src)
        for node in self.nodes:
            print(f"{src} to {node} is {dist[node]} distance")
    
    def dijkstra(self, src):
        dist = dict()
        for n in self.nodes: dist[n] = maxsize
        dist[src] = 0
        sptSet = dict()
        for n in self.nodes: sptSet[n] = False
        for _ in self.nodes:
            m = self.minDistance(dist, sptSet)
            sptSet[m] = True
            for n in self.nodes:
                try: currentDist = self.distances[(m, n)]
                except KeyError: currentDist = 0
                if currentDist > 0 and sptSet[n] == False and dist[n] > dist[m] + currentDist:
                    dist[n] = dist[m] + currentDist
        
        self.print_soln(dist, src)


if __name__ == "__main__":
    g = Graph("ABCDEFGH", distancesOn=True)
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 3)
    g.add_edge('A', 'D', 4)
    g.add_edge('B', 'C', 6)
    g.add_edge('B', 'E', 2)
    g.add_edge('B', 'F', 5)
    g.add_edge('C', 'D', 2)
    g.add_edge('C', 'F', 5)
    g.add_edge('D', 'F', 6)
    g.add_edge('D', 'G', 8)
    g.add_edge('E', 'F', 5)
    g.add_edge('E', 'H', 5)
    g.add_edge('F', 'G', 2)
    g.add_edge('F', 'H', 15)
    g.add_edge('G', 'H', 8)
    g.dkstra('A')