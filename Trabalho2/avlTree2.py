class AVLTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = ListNode(node)
            self.root = node
        else:
            self.root = None

    def insert(self, root, key):

        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        root.h = 1 + max(self.getAltura(root.l),
                         self.getAltura(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.value:
            return self.rRotate(root)

        if b < -1 and key > root.r.value:
            return self.lRotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getAltura(z.l),
                      self.getAltura(z.r))
        y.h = 1 + max(self.getAltura(y.l),
                      self.getAltura(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getAltura(z.l),
                      self.getAltura(z.r))
        y.h = 1 + max(self.getAltura(y.l),
                      self.getAltura(y.r))

        return y

    def getAltura(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getAltura(root.l) - self.getAltura(root.r)


    def levelOrder(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = ArrayQueue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            print(node)
            if node.l:
                queue.push(node.l)
            if node.r:
                queue.push(node.r)
            print(node, end="")