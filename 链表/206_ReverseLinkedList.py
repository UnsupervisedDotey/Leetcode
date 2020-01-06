# 链表节点
class ListNode(object):
    def __init__(self, x):
        self.val = x # 节点值
        self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head, prev = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 迭代思路：重复一定的算法，达到想要的目的。数学上二分法，牛顿法是很好的迭代例子
        # previous = None

        # while head:
        #     new = head
        #     head = head.next          # ? 19行为什么一定不能晚于20和21行
        #     new.next = previous       # 因为new = head, new.next被赋值，head.next也被赋值了 （卧槽）
        #     previous = new

        # return previous

        # 递归思路：在return处调用自己（尾递归）
        if not head:
            return prev

        curr, head.next = head.next, prev    # 新旧链表的两个方向同时前进
        return self.reverseList(curr, head)

# 将列表转换成链表
def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)# 分别将列表中每个数转换成节点
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


# 将链表转换成字符串
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

head = [1,2,3,4,5]
head2 = [4, 5, 8, 9]
s = Solution()


print(listNodeToString(s.reverseList(stringToListNode(head))))  