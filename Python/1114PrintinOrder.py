import threading
class Foo:
    def __init__(self):
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock2:
            printSecond()
            self.lock3.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.lock3:
            printThird()
