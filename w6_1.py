def merge(a, b):
    new_list = []
    d = a + b
    while d:
        new_list.append(d.pop(d.index(min(d))))
    return new_list
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))

A = list(map(int, input().split()))
B = list(map(int, input().split()))


