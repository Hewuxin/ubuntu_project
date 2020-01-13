"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5
"""


def removeNthFromEnd(head, n):
    """一次遍历 两个指针快指针先走到n+1位置，
    然后快慢指针各一步一步的走， 快指针到链表尾
    慢指针到第倒数第n个指针的位置
    i时间复杂度O(L) L为链表节点个数
    空间复杂度O(1)
    """
    if head is None or head.next is None:
        return

    quick = head
    slow = head
    for _ in range(n):
        quick = quick.next

    while slow:
        if quick.next is None:
            break
        else:
            quick = quick.next
            slow = slow.next
    slow.next = slow.next.next
    return head
