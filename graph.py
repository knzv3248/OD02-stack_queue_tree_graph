class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str,  self.graph[vertex])))

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(5, 4)


g.print_graph()