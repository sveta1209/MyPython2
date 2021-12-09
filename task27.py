def distance(x1, y1, x2, y2, x3, y3):
    dist1 = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    dist2 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
    dist3 = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** 0.5
    return dist1 + dist2 + dist3
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
print(distance(x1, y1, x2, y2, x3, y3))
