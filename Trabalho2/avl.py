from array_queue_new import ArrayQueue
from node import ListNode
ROOT = "raiz"


class avl_Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self, data = None, node = None):
        if node:
            self.raiz = node
        elif data:
            node = ListNode(data)
            self.raiz = node
        else:
            self.raiz = None



    def insert_node(self, root, value):

        if not root:
            return avl_Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.avl_BalanceFactor(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def avl_Height(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def avl_BalanceFactor(self, root):
        if not root:
            return 0
        return self.avl_Height(root.left) - self.avl_Height(root.right)

    def avl_MinValue(self, root):
        if root is None or root.left is None:
            return root
        return self.avl_MinValue(root.left)

    def leftRotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a

    def rightRotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.avl_Height(b.left),
                           self.avl_Height(b.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a

    def delete_node(self, root, value):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.avl_MinValue(root.right)
            root.value = temp.key
            root.right = self.delete_node(root.right, temp.value)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.avl_Height(root.left), self.avl_Height(root.right))
        balanceFactor = self.avl_BalanceFactor(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.avl_BalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.avl_BalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end=" ")
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

    def levelOrder(self, node=ROOT):
        if node == ROOT:
            node = self.raiz

        queue = ArrayQueue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            print(node)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end="")







Tree = AVLTree()
list = []
root = None
inf = input("Bem vindo!\n\nPara inserir dados, digite 1\nPara exibir este dado em formato de àrvore AVL, digite 2\n\nSelecione aqui sua opção: ")
while True:

    if inf == "1":
        f = open("entrada.txt", "r")
        lines = f.readline().split()
        f.close()
        for v in range(10):
            list.append(lines[v])
            root = Tree.insert_node(root, list[v])
            print(list)
        inf = input("\n\nDados inseridos!!! Aperte 2 para exibi-lo usando caminhamento por nível. ")
        if inf == "2":
            print(f"\n\nAqui está sua àrvore: \n\n")
            print(f"{Tree.preOrder(root)}\n")
            break
        elif inf == "1":
            inf = input("Você já inseriu os dados. Aperte 2 e veja como sua arvore ficou. ")
        else:
            inf = input("Não consegui entender o que escreveu... escreva novamente. ")
    elif inf == "2":
        inf = input("Você ainda não inseriu sua àrvore. Insira uma e continue com o procedimento. ")
    else:
       inf = input("Não consegui entender o que escreveu... escreva novamente. ")
#root = Tree.insert(root, 1)
#root = Tree.insert(root, 2)
#root = Tree.insert(root, 3)
#root = Tree.insert(root, 4)
#root = Tree.insert(root, 5)
#root = Tree.insert(root, 6)

# Preorder Traversal
#print("")
#Tree.levelOrder(root)
#print()