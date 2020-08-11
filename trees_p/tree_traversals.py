from trees_p.binary_tree import BinaryTree


def preorder(tree):
    if tree is not None:
        print(tree.getNodeValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getNodeValue())


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getNodeValue())
        inorder(tree.getRightChild())
