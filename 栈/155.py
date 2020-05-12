# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._the_min = []
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

        if len(self._the_min) == 0:
            self._the_min.append(x)
        else:
            if x < self._the_min[-1]:
                self._the_min.append(x)
            else:
                self._the_min.append(self._the_min[-1])

    def pop(self) -> None:
        self._the_min.pop()
        return self._data.pop()

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return self._the_min[-1]


minStack = MinStack()
minStack.push(-2)
print(minStack._data, minStack._the_min)
minStack.push(0)
print(minStack._data, minStack._the_min)
minStack.push(-3)
print(minStack._data, minStack._the_min)
# minStack.push(0)
# print(minStack._data, minStack._the_min)
# minStack.getMin()
# print(minStack._data, minStack._the_min)
minStack.pop()
print(minStack._data, minStack._the_min)
minStack.getMin()
print(minStack._data, minStack._the_min)
# minStack.pop()
# print(minStack._data, minStack._the_min)
# minStack.getMin()
# print(minStack._data, minStack._the_min)
# minStack.pop()
# print(minStack._data, minStack._the_min)
# minStack.getMin()
# print(minStack._data, minStack._the_min)