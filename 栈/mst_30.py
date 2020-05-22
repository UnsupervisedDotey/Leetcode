class MinStack:
    """
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = []

    def push(self, x: int) -> None:
        self._stack.append(x)

        if not self._min or x <= self._min[-1]:
            self._min.append(x)

    def pop(self) -> None:
        res = self._stack.pop()
        if res == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def min(self) -> int:
        return self._min[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    print(minStack._stack, minStack._min)
    minStack.push(0)
    print(minStack._stack, minStack._min)
    minStack.push(-3)
    print(minStack._stack, minStack._min)

    minStack.pop()
    print(minStack._stack, minStack._min)
    minStack.top()
    print(minStack._stack, minStack._min)
    minStack.min()
    print(minStack._stack, minStack._min)
