mylist = list(input().split())
a = map(int, mylist)
for i in a:
    if i % 2 == 0:
        print(i, end=' ')

numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
print(' '.join(map(str, numbers)))