from __future__ import annotations
from typing import Union
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        print("?? hi")
        print(root.val)
        cur_node = root
        _1 = 1
        while True:

            if type(cur_node) is not TreeNode:

                _1 *= float(cur_node.left.val == cur_node.right.val)
                cur_node = cur_node.left
            else:
                break

        return bool(_1)


def gen_tree(values: list) -> Union[TreeNode, None]:
    if not values:
        return None
    iter_value = iter(values)
    root = TreeNode(next(iter_value))
    d = deque()
    d.append(root)
    while 1:
        head = d.popleft()
        try:
            head.left = TreeNode(next(iter_value))
            d.append(head.left)
            head.right = TreeNode(next(iter_value))
            d.append(head.right)
        except StopIteration:
            break
    return root


if __name__ == "__main__":
    tree_value = [2,2,1,1,1,None,1]
    tree = gen_tree(tree_value)
    sol = Solution()
    print(sol.isUnivalTree(root=tree))



