a = int(input())
b = int(input())
if b > a:
    b = b + 1
    c = 1
else:
    b = b - 1
    c = -1
for i in range(a, b, c):
    print(i, end=' ')
