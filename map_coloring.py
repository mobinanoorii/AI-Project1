import random

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = dict()

    def add_edge(self, u, v):
        if not u in self.edges:
            self.edges[u] = []
        if not v in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)

    def backtrack_colors(self, v, colors):
        if v > self.n:
            return True

        color_candidates = list(range(4))
        random.shuffle(color_candidates)

        for i in color_candidates:
            ok = True
            for adj in self.edges[v]:
                if colors[adj] == i:
                    ok = False
                    break
            if ok:
                colors[v] = i
                if self.backtrack_colors(v + 1, colors):
                    return True

        colors[v] = -1
        return False

    def color(self):
        colors = dict()
        for i in range(1, self.n + 1):
            colors[i] = -1
        return (self.backtrack_colors(1, colors), colors)

graph = Graph(10)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(1, 5)
graph.add_edge(1, 6)
graph.add_edge(2, 9)
graph.add_edge(2, 10)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(6, 10)
graph.add_edge(7, 8)
graph.add_edge(7, 10)
graph.add_edge(8, 9)
graph.add_edge(8, 10)
graph.add_edge(9, 10)

can_color, color_result = graph.color()

if can_color:
    print("Coloring:")
    for i in range(1, graph.n + 1):
        print(i, ":", color_result[i] + 1)
else:
    print("cannot color his map with 4 colors")