from graphs_p.graph_factory import Graph,Vertex
from graphs_p.graph_factory import StarGraph

def dfs(vert:Vertex):
    dummy=Vertex(0)
    dummy.addNeighbor(vert,0)
    stack=[dummy]
    seen={dummy}
    while len(stack)>0:
        isDeadEnd=True
        v=stack[-1]
        for nbr in v.getConnections():
            if nbr not in seen:
                stack.append(nbr)
                seen.add(nbr)
                isDeadEnd=False
                print(nbr.getId())
                break
        if isDeadEnd:
            stack.pop()


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(5, 2, 1)
    g.addEdge(2, 3, 0)
    g.addEdge(0, 4, 0)
    dfs(g.getVertex(0))
    print('/n')
    g=StarGraph.getDFSInstance()
    dfs(g.getVertex(4))

