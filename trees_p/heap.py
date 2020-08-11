class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2]
                self.heaplist[i // 2] = tmp
            i = i // 2

    def insert(self, k):
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        if self.heaplist[i * 2] > self.heaplist[i * 2 + 1]:
            return i * 2 + 1
        else:
            return i * 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def delMin(self):
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retVal

    def buildHeap(self, buildList):
        i = len(buildList) // 2
        self.currentSize = len(buildList)
        self.heaplist = [0] + buildList
        while i > 0:
            self.percDown(i)
            i -= 1


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.buildHeap([9, 5, 6, 2, 3])

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
