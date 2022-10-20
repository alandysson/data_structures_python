class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __repr__(self):
        l = self.leftChild
        r = self.rightChild
        return(f'[ {self.key}, [{l}], [{r}] ] ')


def constroi_arvore():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.getLeftChild().insertRight('d')
    t.insertRight('c')
    t.getRightChild().insertLeft('e')
    t.getRightChild().insertRight('f')

    return t


arvore = constroi_arvore()
print(arvore)
