class Counter(object):

    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def __str__(self):
        return str(self.counter)

def fib(n,counter):

    counter.increment()

    if n<3:
        return 1

    else:
        return fib(n-1,counter)+fib(n-2,counter)

c= Counter()
problemSize = 2
for i in range(5):
    fib(problemSize,c)
    print(problemSize,c)
    problemSize *= 2


