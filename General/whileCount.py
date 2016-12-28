import time
class Counter(object):

    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def __str__(self):
        return str(self.counter)


def by2(n,counter):
    size = n
    start = time.time()
    while n > 0:
        counter.increment()
        n = n//2

problemSize = 1
c = Counter()

for i in range(10):

    c = Counter()
    by2(problemSize,c)
    print(problemSize,c)
    problemSize *= 10


