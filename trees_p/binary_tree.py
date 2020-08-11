class BinaryTree:
    def __init__(self, val):
        self.key = val
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, val):
        if self.leftChild is None:
            self.leftChild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, val):
        if self.rightChild is None:
            self.rightChild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setNodeValue(self, val):
        self.key = val

    def getNodeValue(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.preorder()


if __name__ == '__main__':
    r = BinaryTree('a')
    baseRoot = r
    print(r.getNodeValue())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getNodeValue())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getNodeValue())
    r.getRightChild().setNodeValue('hello')
    print(r.getRightChild().getNodeValue())
    print('preorder:\n')
    baseRoot.preorder()
    print('\n postorder: \n')
    baseRoot.postorder()
    print('\n inorder: \n')
    baseRoot.inorder()
