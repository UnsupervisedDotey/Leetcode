class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack_in = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack_in.append(x)
        self._stack_out = []

        tmp = self._stack_in.copy()

        while self._stack_in:
            self._stack_out.append(self._stack_in.pop())

        self._stack_in = tmp

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self._stack_out.pop()

        self._stack_in = []

        tmp = self._stack_out.copy()

        while self._stack_out:
            self._stack_in.append(self._stack_out.pop())

        self._stack_out = tmp

        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._stack_in) == 0


if __name__ == "__main__":
    s = MyQueue()
    s.push(1)
    print(s._stack_out,s._stack_in)
    s.push(2)
    print(s._stack_out, s._stack_in)
    s.peek()
    print(s._stack_out, s._stack_in)
    s.pop()
    print(s._stack_out, s._stack_in)
    s.empty()
    print(s._stack_out, s._stack_in)
