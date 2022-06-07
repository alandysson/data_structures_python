from random import randint


def bumbleSort(list):
    for i in range(len(list) - 1):
        for x in range(i):
            if list[x] > list[x + 1]:
                temp = list[x]
                list[x] = list[x + 1]
                list[x + 1] = temp

    return list


x = []
for i in range(8):
    x.append(randint(1, 15))
print(x)
print(bumbleSort(x))
