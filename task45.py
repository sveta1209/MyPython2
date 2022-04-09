
def Intersection(a, b):
    c = sorted(list(set(a) & set(b)))
    print(c)
    return c

a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = Intersection(a, b)

print(*d)