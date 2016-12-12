import ctypes
import sys


class DyArray(object):
    def __init__(self):

        self.length = 0
        self.capacity = 1
        self.A = self.makeArray(self.capacity)

    def lenArray(self):

        return self.length

    def getElement(self, k):

        if not 0 <= k < self.length:
            return IndexError("Array Index out of Bounds")
        else:
            return self.A[k]

    def appendElement(self, element):

        if self.length == self.capacity:
            self.resize(2 * self.capacity)

        self.A[self.length] = element
        self.length += 1


    def resize(self, new_cap):
        B = self.makeArray(new_cap)

        for k in range(self.length):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def makeArray(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def __str__(self):

        s = "["
        for k in range(self.length):
            s = s + str(self.A[k]) + ','

        s = s + "]"
        return s

    def getsize(self):
        return sys.getsizeof(self.A)

    def __sizeof__(self):
        print("I am here")
        return 1000


l = DyArray()
print(l.getsize())
l.appendElement(3)
print(l.getsize())
l.appendElement(3)
l.appendElement(3)
l.appendElement(3)
print(l.getsize())

