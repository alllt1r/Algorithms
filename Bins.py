from random import randint
from datetime import *
array = [randint(1, 10000) for i in range(100)]
def binSearch(arr, key):
    array.sort()
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    while arr[mid] != key and low <= high:
        mid = (low + high) // 2
        if key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        print('Таких значений там нет!')
    else:
        print(f'Номер элемента в массиве: {mid}.')

print(sorted(array))
question = int(input('Какое число надо найти в массиве?'))
start = datetime.now()
binSearch(array, question)
finish = datetime.now() - start
print(finish)