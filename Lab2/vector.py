from array import array
from typing import Iterable

def _length_check_decorator(func):
    def checker(self, *arg, **kwargs):        
        if self._current_len == self._max_len:
            self._max_len *= 2
            temp = self._array
            self._array = array(self.type, [0]*self._max_len)
            for i in range(0, self._current_len):
                self._array[i] = temp[i]
        return func(self, *arg, **kwargs)

    return checker

def _non_int_checker(func):
    def checker(self, *arg, **kwargs):
        for item in arg or kwargs.values():
            if type(item) != int:
                raise NotImplementedError("The Vector can only contain numbers")

        return func(self, *arg, **kwargs)

    return checker
    
def _index_checker_decorator(func):
    def checker(self, index, *arg, **kwargs):
        if index > self._current_len or index < 0:
            raise IndexError("Index out of range")

        return func(self, index, *arg, **kwargs)

    return checker

class Vector():
    def __init__(self, iterable: Iterable = None):
        self._max_len = 2
        self._current_len = 0
        self.type = "i"
        self._array = array(self.type, [0]*self._max_len)
        
        if hasattr(iterable, '__iter__'):
            for i in iterable:
                if type(i) != int:
                    raise NotImplementedError("Number Only")
                self.append(i)

    def __iter__(self):
        return self._array.__iter__()

    def __str__(self):
        return self._array.__str__()

    def __repr__(self) -> str:
        s = "Vector("
        for i in range(0, self._current_len):
            s += f"{self._array[i]}, "

        if self._current_len > 0:
            return s[:-2] + ")"
        return s + ")"

    def length(self):
        return self._current_len
    
    def contains(self, item):
        if item in self._array and self._current_len:
            return True

        return False

    @_index_checker_decorator
    def getitem(self, index):
        if self._current_len == index == 0:
            return None

        return self._array[index]
    
    @_non_int_checker
    @_index_checker_decorator
    @_length_check_decorator
    def setitem(self, index, item):
        if index == self._current_len:
            self._current_len += 1
            self._array[index] = item
        else:
            self._array[index] = item

    @_non_int_checker
    @_length_check_decorator
    def append(self, item):
        self._array[self._current_len] = item
        self._current_len += 1
    
    @_non_int_checker
    @_index_checker_decorator
    @_length_check_decorator
    def insert(self, index, item):
        self._current_len += 1
        temp = array(self.type, [0]*self._max_len)
        j = 0
        for i in self._array:
            if j == index:
                temp[j] = item
                j += 1

            temp[j] = i
            j += 1

            if j >= self._current_len:
                break

        self._array = temp
            
    @_index_checker_decorator
    @_length_check_decorator
    def remove(self, index):
        self._current_len -= 1
        temp = array(self.type, [0]*self._max_len)
        j = 0
        removed = False
        for i in self._array:            
            if j == index and not removed:
                removed = True
                continue

            temp[j] = i
            j += 1

            if j >= self._current_len:
                break

        self._array = temp

    def indexOf(self, item):
        for j, i in enumerate(self._array):
            if j >= self._current_len:
                break
            if i == item:
                return j
        return -1

    def extend(self, otherVec):
        for i in otherVec:
            self.append(i)

    def subVector(self, fromIndex, toIndex):
        toIndex += 1
        diff = toIndex-fromIndex
        if diff <= 0:
            raise IndexError("To Index is smaller than From Index")
        if fromIndex < 0:
            raise IndexError("From index can't be negative")
        if toIndex > self._current_len:
            raise IndexError("To Index can't be higher than current length - 1")

        temp = Vector([0]*diff)

        for j, i in enumerate(range(fromIndex, toIndex)):
            temp.setitem(j, self._array[i])
        
        return temp

if __name__ == "__main__":
    v1 = Vector()
    print(f"{v1 = }")

    print(f"{v1.length() = }")

    print(f"{v1.contains(0) = }")

    print(f"{v1.getitem(0) = }")

    v1.setitem(index = 0, item = 2)
    print(f"setitem: {v1 = }")

    v1.append(10)
    print(f"append: {v1 = }")

    v1.insert(index = 1, item = 1)
    print(f"insert: {v1 = }")

    v1.remove(0)
    print(f"remove: {v1 = }")

    print(f"{v1.indexOf(10) = }")

    v2 = Vector([1, 2, 3, 4, 5, 6, 7, 8])
    v1.extend(v2)
    print(f"extend: {v1 = }")

    sub = v1.subVector(1, 6)
    print(f"subVector: {sub = }")