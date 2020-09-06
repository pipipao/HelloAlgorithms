from graphs_p.graph import Graph, Vertex
from graphs_p.graph_factory import StarGraph, RecGraph


# https://www.jianshu.com/p/70952b51f0c8
def bfs(vert: Vertex):
    seen = {vert}
    queue = [vert]
    while len(queue) > 0:
        v = queue.pop(0)
        print(v.getId())
        for nbr in v.getConnections():
            if nbr not in seen:
                queue.append(nbr)
                seen.add(nbr)


if __name__ == '__main__':
    g = StarGraph.getBFSInstance()
    bfs(g.getVertex(1))
