class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        dict = {}
        while head:
            if id(head) in dict:
                return True
            else:
                dict[id(head)] = True
            head = head.next
        return False
        """

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False



def stringToListNode(input):
    numbers = input
    dummyRoot = Node(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = Node(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


head = [1,2,3,4,5]
head2 = [4, 5]
s = Solution()


# print(listNodeToString(s.getIntersectionNode(stringToListNode(head), stringToListNode(head2))))
# print(s.hasCycle(stringToListNode([1, 2, 3, 1, 2, 3])))

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
print(s.hasCycle(node1))

