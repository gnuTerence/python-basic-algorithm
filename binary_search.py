import random
import math
import time

start_time = time.time()

def binary_search(lst, pos):
    low = 0
    high = len(lst)
    while low <= high:
        mid = (low+high)//2
        guess = lst[mid]
        if guess == pos:
            return mid
        if guess > pos:
            high = mid - 1
        else: 
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 10]

num = random.randint(0, len(my_list)-1)

item = my_list[num]

print('Item = ', item)

print('Item Position: ',binary_search(my_list, item))

print("Process finished --- %s seconds ---" % (time.time() - start_time))