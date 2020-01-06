class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def mergeTwoLists(self, l1, l2):

        head = ListNode(0)
        cur = head          # cur使head变成一串
                            # cur是个中间变量？

        while l1 is not None and l2 is not None:

            if l1.val <= l2.val:
                cur.next = l1       # 新链 添加下位
                l1 = l1.next        # 旧链2 上顶
            else:
                cur.next = l2       # 新链 添加下位
                l2 = l2.next        # 旧链2 上顶

            cur = cur.next          # 新链 新下位の上顶

        if l1 != None:              #############################
            cur.next = l1           #                           #
                                    #   temp.next = l1 or l2    #
        if l2 != None:              #                           #
            cur.next = l2           #############################

        return head.next


def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
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


head = [1, 2, 4]
head2 = [1, 3, 4]
s = Solution()


print(listNodeToString(s.mergeTwoLists(stringToListNode(head), stringToListNode(head2))))