class MaxHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def insert(self,k):
        self.heapList.append(k)
        self.heapSize += 1
        self.percUp(self.heapSize)

    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    def delMax(self):
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return self.heapList[1]

    def percDown(self,i):
        while i * 2 < self.heapSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def maxChild(self,i):
        if i*2+1 > self.heapSize:
            return i*2

        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def __str__(self):
        return str(self.heapList)


m = MaxHeap()
m.insert(5)
m.insert(3)
m.insert(15)
m.insert(51)
m.insert(34)
m.insert(125)
m.insert(25)
m.insert(53)
m.insert(12)
m.insert(9)
m.insert(43)
m.insert(985)
print(m)
m.delMax()
print(m)

