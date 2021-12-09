hh1 = int(input())
mm1 = int(input())
ss1 = int(input())
hh2 = int(input())
mm2 = int(input())
ss2 = int(input())
sec1 = hh1 * 3600 + mm1 * 60 + ss1
sec2 = hh2 * 3600 + mm2 * 60 + ss2
dif = sec2 - sec1
print(dif)
hh = dif // 3600
mm = (dif % 3600) // 60
ss = (dif % 3600) % 60
print(hh % 24, ':', mm // 10, mm % 10, ':', ss // 10, ss % 10, sep='')
