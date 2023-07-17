import time
import random
start_time = time.time()

a = []

for i in range(0, 1000):
    num = random.randint(0, 1000)
    a.append(num)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(a))

print("Process finished --- %s seconds ---" % (time.time() - start_time))

