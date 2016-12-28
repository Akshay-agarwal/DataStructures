class MinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    def ins(self,k):
        self.heapList.append(k)
        self.heapSize += 1
        self.percUp(self.heapSize)

    def percDown(self,i):
        while i * 2 < self.heapSize:
            mc = self.minChild(i)

            if self.heapList[mc] < self.heapList[i]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def minChild(self,i):
        if i*2+1 > self.heapSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return self.heapList[1]

    def __str__(self):
        return str(self.heapList)

m = MinHeap()
m.ins(3)
m.ins(10)
m.ins(5)
m.ins(12)
m.ins(1)
print(m)
