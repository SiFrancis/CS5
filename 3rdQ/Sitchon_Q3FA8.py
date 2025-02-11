from queue import Queue

class Graph:
    def __init__(self):
        self.graph = dict()
        self.nodes = self.graph.keys()
    
    def add_edge(self, src, dst):
        self.graph[src].add(dst)
        if dst not in self.nodes: 
            self.graph[dst] = set()
        self.graph[dst].add(src)
    
    def print_graph(self):
        # adjacency list
        print("ADJACENCY LIST")
        print(self.graph)
    
    def bfs(self, src):
        visited = {node: False for node in self.nodes}
        output = []
        queue = Queue()
        
        s = src
        visited[s] = True
        queue.put(s)
        
        while not queue.empty():
            u = queue.get()
            output.append(u)
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.put(v)
        
        print("BFS Output: ", output)
    
    def dfs(self, src, visited):
        if src not in visited:
            print(src)
            visited.add(src)
            for neighbor in self.graph[src]:
                self.dfs(neighbor, visited)
    
    def input_nodes(self):
        print("Enter the names of the graph nodes, separated by newlines (type !exit to stop input):")
        running1 = True
        node_count = 1
        while running1:
            node = input(f"Enter name of node {node_count}: ")
            if node == "!exit": running1 = False
            else:
                print(f"Enter the neighbors of Node {node} (use !exit to stop):")
                running2 = True
                self.graph[node] = set()
                node_count += 1
                neighbor_count = 1
                while running2:
                    neighbor = input(f"Enter neighbor {neighbor_count} of node {node}: ")
                    if neighbor == "!exit": running2 = False
                    else:
                        self.add_edge(node, neighbor)
                        neighbor_count += 1
    
    def input_search(self):
        while True:
            choice = input("Choose [B]FS or [D]FS search (or exit with !exit): ")
            if choice == 'B':
                while True:
                    src_in = input("Choose source node of BFS search: ")
                    if src_in not in self.nodes: print("INVALID: Node does not exist in graph")
                    else: break
                self.bfs(src_in)
            elif choice == 'D':
                while True:
                    src_in = input("Choose source node of DFS search: ")
                    if src_in not in self.nodes: print("INVALID: Node does not exist in graph")
                    else: break
                v = set()
                self.dfs(src_in, v)
            elif choice == '!exit': break
            else:
                print("INVALID: Enter only [B], [D], or !exit")

if __name__ == "__main__":
    g = Graph()
    g.input_nodes()
    print()
    g.print_graph()
    print()
    g.input_search()