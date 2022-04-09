def CountSort(A):
    new_list = [0] * 101
    for element in A:
        new_list[element] += 1
    for nowelement in range(101):
        print((str(nowelement) + ' ') * new_list[nowelement], end='')

n = list(map(int, input().split()))
CountSort(n)
