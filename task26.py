def dist(x1, y1, x2, y2):
    dist = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    return dist
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(dist(x1, y1, x2, y2))
