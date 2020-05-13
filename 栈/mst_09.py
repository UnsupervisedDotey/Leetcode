"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

"""


class CQueue:

    def __init__(self):
        self._stack_in = []
        self._stack_out = []

    def appendTail(self, value: int) -> None:
        self._stack_in.append(value)
        self._stack_out = []
        tmp = self._stack_in.copy()
        while self._stack_in:
            self._stack_out.append(self._stack_in.pop())
        self._stack_in = tmp

    def deleteHead(self) -> int:
        try:
            res = self._stack_out.pop()
        except:
            return -1
        self._stack_in = []
        tmp = self._stack_out.copy()
        while self._stack_out:
            self._stack_in.append(self._stack_out.pop())
        self._stack_out = tmp
        return res


if __name__ == "__main__":
    # Your CQueue object will be instantiated and called as such:
    obj = CQueue()
    for i in range(10):
        obj.appendTail(i)
        print(obj._stack_in, obj._stack_out)

    param_2 = obj.deleteHead()
    print(obj._stack_in, obj._stack_out)
