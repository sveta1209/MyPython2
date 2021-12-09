A = int(input())
B = int(input())

diff = ((A - B)**2)**.5
print(diff)
max_num = int((A + B + diff) // 2)

print(max_num)
