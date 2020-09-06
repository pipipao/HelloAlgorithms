from graphs_p.graph_factory import Graph,Vertex
from graphs_p.graph_factory import StarGraph

def dfs(vert:Vertex):
    stack=[vert]
    seen={vert}
    while len(stack)>0:
        isDeadEnd=True
        v=stack[-1]
        for nbr in v.getConnections():
            if nbr not in seen:
                stack.append(nbr)
                seen.add(nbr)
                isDeadEnd=False
                break
        if isDeadEnd:
            print(v.getId())
            stack.pop()


if __name__ == '__main__':
    g=StarGraph.getDFSInstance()
    dfs(g.getVertex(4))

