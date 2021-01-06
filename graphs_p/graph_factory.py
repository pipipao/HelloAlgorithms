from graphs_p.graph import Graph,Vertex
class StarGraph:
    @staticmethod
    def getBFSInstance():
        g=Graph()
        g.addEdge(1,2)
        g.addEdge(1,3)
        g.addEdge(2,3)
        g.addEdge(2,4)
        g.addEdge(3,2)
        g.addEdge(3,3)
        g.addEdge(3,4)
        g.addEdge(4,1)
        g.addEdge(5,4)
        g.addEdge(5,3)
        return g

    @staticmethod
    def getDFSInstance():
        g = Graph()
        g.addEdge(1, 2)
        g.addEdge(1, 3)
        g.addEdge(2, 3)
        g.addEdge(2, 5)
        g.addEdge(3, 3)
        g.addEdge(4, 1)
        g.addEdge(4, 5)
        g.addEdge(5, 3)
        return g

class RecGraph:
    @staticmethod
    def getInstance():
        g = Graph()
        g.addEdge('A', 'B')
        g.addEdge('B', 'C')
        g.addEdge('A', 'D')
        g.addEdge('B', 'D')
        g.addEdge('D', 'E')
        g.addEdge('E', 'B')
        g.addEdge('E', 'F')
        g.addEdge('F', 'C')
        return g