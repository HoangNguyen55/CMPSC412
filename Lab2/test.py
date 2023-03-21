from array import array
def decorator(fn):
    def _decorator(self, *arg):
        print(f"I'm decorating, and here's my list: {self.b}")
        fn(self, *arg)
    return _decorator

class test():
    def __init__(self) -> None:
        self.test = 3
        self.b = array("i", [1, 2])
    @decorator
    def func(self, arg):
        self.test = arg
        print(self.b)

a = test()
a.b.extend([1, 2 ,3])
a.func(6)