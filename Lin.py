class Node(object):
  def __init__(self,value,next):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.start = None
    self.end = None
    self.leng = 0

  def lengthOfLl(self):
    return self.leng

  def append(self,ele):
    n = Node(ele,None)

    if self.start == None:
      self.start = n
      self.leng += 1

    else:
      self.end.next = n
      self.leng += 1


    self.end = n
    self.end.next = self.start

  def getN(self,i):
    current = self.start
    for j in range(i):
      if current is None:
        return None
      else:
        current = current.next
    return current.value

  def __str__(self):
    s = '['
    current = self.start
    for i in range(self.leng):
      s = s+str(current.value)+','
      current = current.next
    s = s + ']'
    return s

l = LinkedList()
l.append(2)
l.append(3)
l.append(5)
l.append(2)
l.append(3)
l.append(5)
l.append(2)
l.append(3)
l.append(5)
l.append(2)
l.append(3)
l.append(5)
print(l)
print(l.lengthOfLl())
print(l)

