from __future__ import annotations
from typing import Union
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1



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
    tree_value = [1,1,1,1,1,None,1]
    tree = gen_tree(tree_value)
    sol = Solution()
    print(sol.isUnivalTree(root=tree))



