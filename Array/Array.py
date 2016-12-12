import ctypes
import sys

class Array(object):

    def __init__(self):
        self.length =0
        self.capactiy=1
        self.A = self.makeArray(self.capactiy)

    def arrayLength(self):
        return self.length

    def getElement(self,k):
        if not 0<k<self.length:
            return "Please Enter a number less than Array size."
        else:
            return self.A[k]

    def appendElement(self,ele):
        if self.length == self.capactiy:
            self.resize(2*self.capactiy)

        self.A[self.length] = ele
        self.length += 1

    def resize(self,new_cap):
        B = self.makeArray(new_cap)

        for i in range(self.length):
            B[i] = self.A[i]

        self.A = B
        self.capactiy = new_cap

    def makeArray(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def __str__(self):
        s= '['
        for j in range(self.length):
            s=s+str(self.A[j])+','

        s = s +']'
        return s

a = Array()
a.arrayLength()
a.appendElement(2);
a.appendElement(3);
print(a)
print(a.arrayLength())
