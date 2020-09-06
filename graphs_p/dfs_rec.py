from graphs_p.graph import Graph, Vertex
from graphs_p.graph_factory import StarGraph


def dfs(vert: Vertex):
    seen = {vert}
    _dfs(vert,seen)


def _dfs(vertex: Vertex,seen:set):
    for v in vertex.getConnections():
        if v not in seen:
            seen.add(v)
            _dfs(v,seen)
    print(vertex.getId())


if __name__ == '__main__':
    g = StarGraph.getDFSInstance()
    dfs(g.getVertex(4))
