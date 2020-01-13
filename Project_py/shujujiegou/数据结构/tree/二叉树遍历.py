class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = list()
        queue.append(self.root)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    # def add(self, item):
        # node = Node(item)
        # if self.root is None:
        #     self.root = node
        #     return
        # queue = list()
        # queue.append(self.root)
        # while queue:
        #     cur_node = queue.pop(0)
        #     if cur_node.lchild is None:
        #         cur_node.lchild = node
        #         return
        #     else:
        #         queue.append(cur_node.lchild)
        #     if cur_node.rchild is None:
        #         cur_node.rchild = node
        #         return
        #     else:
        #         queue.append(cur_node.rchild)

    def travel(self):
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.elem, end="")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def preordertravel(self, node):
        if node is None:
            return
        print(node.elem, end="")
        self.preordertravel(node.lchild)
        self.preordertravel(node.rchild)

    def inordertravel(self, node):
        if node is None:
            return
        self.inordertravel(node.lchild)
        print(node.elem, end="")
        self.inordertravel(node.rchild)

    def postordertravel(self, node):
        if node is None:
            return
        self.postordertravel(node.lchild)
        self.postordertravel(node.rchild)
        print(node.elem, end="")

    def pre(self, root):
        white, gray = 0, 1
        res = []
        stack = list()
        stack.append((white, root))

        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == white:
                stack.append((white, node.rchild))
                stack.append((white, node.lchild))
                stack.append((gray, node))
            else:
                res.append(node.elem)
        return res



if __name__ == "__main__":
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    print("广度遍历")
    t.travel()
    print()
    print("preorder")
    t.preordertravel(t.root)
    print()
    print("inorder")
    t.inordertravel(t.root)
    print()
    print("post")
    t.postordertravel(t.root)
    print("pre", t.pre(t.root))
