n = int(input())
sd = list(map(int, input().split()))
sd_t = []
for i in range(n):
    sd_t.append((sd[i], i + 1))
sd_t.sort()


m = int(input())
bd = list(map(int, input().split()))
bd_t = []
for i in range(m):
    bd_t.append((bd[i], i + 1))
bd_t.sort()

res = [0] * n

fb = 0

for i in range(0, n):
    dist = sd_t[i][0] + bd_t[0][0]
    j = fb
    while j < m and abs(sd_t[i][0] - bd_t[j][0]) < dist:
        if abs(sd_t[i][0] - bd_t[j][0]) < dist:
            dist = abs(sd_t[i][0] - bd_t[j][0])
            res[sd_t[i][1] - 1] = bd_t[j][1]
            fb = j
        j += 1

print(*res)
