class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elm in self.leftChild:
                    yield elm
            yield self.key
            if self.hasRightChild():
                for elm in self.rightChild:
                    yield elm


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        if currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
        return None

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        return False

    def findMax(self, rootNode):
        if rootNode.hasRightChild():
            return self.findMax(rootNode.rightChild)
        return rootNode

    def findMin(self, rootNode):
        if rootNode.hasLeftChild():
            return self.findMin(rootNode.leftChild)
        return rootNode

    def removeNode(self, node):
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild = None
            elif node.isRightChild():
                node.parent.rightChild = None
            else:
                self.root = None
        elif not node.hasBothChildren():
            if node.isLeftChild():
                if node.hasLeftChild():
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                else:
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
            elif node.isRightChild():
                if node.hasLeftChild():
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                else:
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
            else:
                if node.hasLeftChild():
                    node.replaceData(node.leftChild.key,
                                     node.leftChild.leftChild,
                                     node.leftChild.rightChild)
                    node.parent = None
                if node.hasRightChild():
                    node.replaceData(node.rightChild.key,
                                     node.rightChild.leftChild,
                                     node.rightChild.rightChild)
                    node.parent = None
        else:
            successor = self.findMin(node.rightChild)
            node.key = successor.key
            node.value = successor.val
            self.removeNode(successor)

    def delete(self, key):
        if self.size > 0:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.removeNode(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        else:
            raise KeyError('Error, tree is empty')

    def __delitem__(self, key):
        self.delete(key)


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[5]=5
    mytree[3]=3
    mytree[1]=1
    mytree[4]=4
    mytree[6]=6
    mytree[7]=7
    mytree.delete(5)


    print(mytree[3])
    print(mytree[2])
