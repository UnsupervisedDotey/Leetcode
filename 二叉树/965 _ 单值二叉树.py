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
            head.l_node = TreeNode(next(iter_value))
            d.append(head.l_node)
            head.r_node = TreeNode(next(iter_value))
            d.append(head.r_node)
        except StopIteration:
            break
    return root


def pre_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield node.value
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)


def in_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield node.value
    yield from pre_traverse_tree(node.r_node)


def post_traverse_tree(node: TreeNode):
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)
    yield node.value



if __name__ == "__main__":

    tree = gen_tree(list(range(10)))
    print(list(pre_traverse_tree(tree)))
    print(list(in_traverse_tree(tree)))
    print(list(post_traverse_tree(tree)))

    tree_value = [1,1,1,1,1,None,1]
    for i in range(len(tree_value)):
        c1 = add_node_in_order(elements)
