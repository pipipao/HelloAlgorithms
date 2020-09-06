from graphs_p.graph import Graph,Vertex


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    return False


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for cmd in moveOffsets:
        newX = x + cmd[0]
        newY = y + cmd[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((x, y))
    return newMoves


def posToNodeId(row, col, bdSize):
    return (row * bdSize) + col


def knightGraph(bdSize):
    g = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId=posToNodeId(row,col,bdSize)
            newPositions=genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid=posToNodeId(e[0],e[1],bdSize)
                g.addEdge(nodeId,nid)
    return g

def knightTour(n,havePased:list,vert:Vertex,limit):
    havePased.append(vert)
    done = False
    if n<limit:
        nbrList=list(vert.getConnections())
        for v in nbrList:
            if done:
                break
            if v not in havePased:
                done=knightTour(n+1,havePased,v,limit)
        if not done:
            havePased.pop()
    else:
        done=True
    return done


if __name__ == '__main__':
    myl=[]
    g=Graph()
    g.addEdge('A','B')
    g.addEdge('B','C')
    g.addEdge('A','D')
    g.addEdge('B','D')
    g.addEdge('D','E')
    g.addEdge('E','B')
    g.addEdge('E','F')
    g.addEdge('F','C')
    print(g.getVertices())
    knightTour(1,myl,g.getVertex('A'),6)
    for v in myl:
        print(v.getId())
