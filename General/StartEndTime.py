import time

problemSize = 40000000;

# calculate start time
start = time.time()

work = 1
for i in range(problemSize):
    i += 1
    i -= 1

# end time
totalTime = time.time()- start

print(problemSize,totalTime)
