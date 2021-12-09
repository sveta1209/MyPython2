#проверка на четность
number = int(input())
isEven = number % 2 == 0
print(isEven)

#пересечение отрезков
a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
answer = a <= b1 and a1 <= b
print(answer)
