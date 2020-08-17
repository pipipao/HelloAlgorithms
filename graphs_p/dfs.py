from graphs_p.graph import Graph, Vertex


def DFS(graph, s):
    stack = [s]
    seen = set()
    seen.add(s)
    print(s)
    while len(stack) > 0:
        vertex = stack.pop()
        for w in vertex.getConnections():
            if w not in seen:
                stack.append(vertex)
                stack.append(w)
                seen.add(w)
                print(w)
                break


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 1)
    g.addEdge(2, 3, 0)
    g.addEdge(0, 4, 0)
    DFS(g, g.getVertex(0))
