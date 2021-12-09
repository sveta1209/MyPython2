x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
r = float(input())
def isPointInCircle(x1, y1, x2, y2, r):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r ** 2
if isPointInCircle(x1, y1, x2, y2, r):
     print('YES')
else:
    print('NO')
