from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    def Dfs(self,s):

        stack, visited = set(), [s]

        while stack:
            vertex =stack.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph(vertex)-visited)
        return visited

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
vertex = g.Dfs(2)
print(list(vertex))

