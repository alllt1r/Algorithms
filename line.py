from random import randint
array = [randint(1, 10000) for i in range(100)]
array.sort()
print(array)
key = int(input('Введите число'))
for ch in range(100):
    if array[ch] == key:
        print(ch)
