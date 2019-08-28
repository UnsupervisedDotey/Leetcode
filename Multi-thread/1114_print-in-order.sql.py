from threading import Condition, Thread


def One():
    print('one', end='')


def Two():
    print('two', end='')


def Three():
    print('three', end='')


class Foo:
    def __init__(self):
        self.cd = Condition()
        self.NUM = 0

    def first(self, PrintFirst: callable):
        # 这里使用with语法糖
        with self.cd:
            while self.NUM != 0:
                self.cd.wait()
            self.cd.acquire()
            PrintFirst()
            self.NUM += 1
            self.cd.notify_all()
            self.cd.release()

    def second(self, PrintSecond: callable):
        self.cd.acquire()
        while self.NUM != 1:
            self.cd.wait()
        PrintSecond()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()

    def third(self, PrintThird: callable):
        self.cd.acquire()
        while self.NUM != 2:
            self.cd.wait()
        PrintThird()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()


if __name__ == '__main__':
    foo = Foo()
    callablelist = [foo.first, foo.second, foo.third]
    callablelistargs = [One, Two, Three]
    order = [2, 1, 3]
    A = Thread(target=callablelist[order[0] - 1], args=(callablelistargs[order[0] - 1],))
    B = Thread(target=callablelist[order[1] - 1], args=(callablelistargs[order[1] - 1],))
    C = Thread(target=callablelist[order[2] - 1], args=(callablelistargs[order[2] - 1],))
    A.start()
    B.start()
    C.start()

# python多线程-Semaphore(信号对象)
# 也有acquire和release
#
# from threading import *
#
#
# class Foo:
#     def __init__(self):
#         self.s1 = Semaphore(1)
#         self.s2 = Semaphore(0)
#         self.s3 = Semaphore(0)
#
#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         # printFirst() outputs "first". Do not change or remove this line.
#         self.s1.acquire()
#         printFirst()
#         self.s2.release()
#
#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         # printSecond() outputs "second". Do not change or remove this line.
#         self.s2.acquire()
#         printSecond()
#         self.s3.release()
#
#     def third(self, printThird: 'Callable[[], None]') -> None:
#         # printThird() outputs "third". Do not change or remove this line.
#         self.s3.acquire()
#         printThird()