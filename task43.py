n = int(input())
s1 = '+___ '
s3 = '|__\\ '
s4 = '|    '
print(s1 * n)
for i in range(1, n + 1):
    print('|', i, ' / ', sep='', end='')
print()
print(s3 * n)
print(s4 * n)
