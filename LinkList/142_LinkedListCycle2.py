# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = q = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while (q != slow):
                    q = q.next
                    slow = slow.next
                return q
        return None



s = Solution()
#创建一个链表
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
print(s.detectCycle(node1))

