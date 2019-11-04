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
        return True


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


def pre_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield node.val
    yield from pre_traverse_tree(node.left)
    yield from pre_traverse_tree(node.right)


def in_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.left)
    yield node.val
    yield from pre_traverse_tree(node.right)


def post_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.left)
    yield from pre_traverse_tree(node.right)
    yield node.val



if __name__ == "__main__":
    tree_value = [1,1,1,1,1,None,1]
    tree = gen_tree(tree_value)
    print(list(pre_traverse_tree(tree)))
    print(list(in_traverse_tree(tree)))
    print(list(post_traverse_tree(tree)))

    

