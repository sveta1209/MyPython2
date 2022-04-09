a = int(input())
b = sorted(set(list(map(int, input().split()))))
n = []
for i in b:
    if i - a >= 3 or i - a == 0:
        n.append(i)
        a = i
print(len(n))
