N = int(input())
hh = N // 3600
mm = (N % 3600) // 60
ss = (N % 3600) % 60
print(hh % 24, ':', mm // 10, mm % 10, ':', ss // 10, ss % 10, sep='')
