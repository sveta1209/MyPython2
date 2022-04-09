def Intersection(a, b):
    new_list = sorted(list(set(a) & set(b)))
    return new_list
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))
