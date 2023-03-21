# first in last out
class stack():
    def __init__(self) -> None:
        self._internal_list = []

    def isEmpty(self):
        return not bool(len(self._internal_list))

    def push(self, item):
        self._internal_list.append(item)

    def pop(self):
        return self._internal_list.pop()
    
    def peek(self):
        return self._internal_list[-1]

    def size(self):
        return len(self._internal_list)


# first in first out
class queue():
    def __init__(self) -> None:
        self._stack_in = stack()
        self._stack_out = stack()

    def enqueue(self, item):
        self._stack_in.push(item)

    def dequeue(self):
        for _ in range(self._stack_in.size() - 1):
            self._stack_out.push(self._stack_in.pop())

        temp = self._stack_in.pop()

        for _ in range(self._stack_out.size()):
            self._stack_in.push(self._stack_out.pop())


        return temp

def bracket_checker(string: str):
    s = stack()
    
    # race condition
    if len(string) == 1:
        return False

    for i in string:
        if i in ['{', '[', '(']:
            s.push(i)
        elif i in ['}', ')', ']']:
            try:
                v = s.pop()
            except IndexError:
                return False
            if (v == '{' and i != '}')\
            or (v == '[' and i != ']')\
            or (v == '(' and i != ')'):
                return False

    return True

q = queue()
for i in range(10):
    q.enqueue(i)

for _ in range(10):
    print(f"{q.dequeue() = }")

print(f"{bracket_checker('[') = }")