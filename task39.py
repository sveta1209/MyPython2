a = [1, 2, 3 , 4]
b = a
a = [3, 4]
print(b)
print(a)

nowList = list('abcdef')
print(nowList)

def reverseList(funcList):
    funcList = funcList[::-1]
    
mainList = list('abc')
reverseList(mainList)
print(*mainList)
print(mainList)
s = ",".join(mainList)
print(s)
print('abc d d 123 djfhb     dnj'.split())

z = input().split('1')
print(z)
