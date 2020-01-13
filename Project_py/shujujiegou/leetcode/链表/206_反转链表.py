class Node(object):
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def travel(self):
        if self.head is None:
            return
        cur = self.head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def reverseList(self):
        """双指针迭代"""
        pre = None
        cur = self.head
        while cur:
            # 保存当前节点的下一节点
            tmp = cur.next
            # 将当前节点指向pre
            cur.next = pre
            # pre cur 各向前一步
            pre = cur
            cur = tmp
        return pre

    def reverseList01(self, node):
        """递归实现"""
        if node is None or node.next is None:
            return node

        else:
            new_node = self.reverseList01(node.next)
            node.next.next = node
            node.next = None
            return new_node


if __name__ == "__main__":
    ll = LinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    print(ll.travel())
    print("fanzhuan list")
    ll.reverseList01(ll.head)
    print(ll.travel())
