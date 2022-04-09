N = int(input())
x = []
for i in range(N):
    x.append(list(input().split()))
    x[i][1] = int(x[i][1])
    x[i][0], x[i][1] = x[i][1], x[i][0]
x.sort(reverse=True)
for i in range(N):
    print(x[i][1])
