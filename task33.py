def IsPrime(n):
    i = 2
    while n % i != 0 or i == n:
        i += 1
        if i > n**0.5:
            return 'YES'
    return 'NO'

print(IsPrime(int(input())))

def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
rec()
