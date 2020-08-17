from graphs_p.graph import Graph, Vertex


def BFS(graph, s):
    queue = [s]
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        for w in vertex.getConnections():
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 1)
    g.addEdge(2, 3, 0)
    g.addEdge(0, 4, 0)
    BFS(g, g.getVertex(0))
