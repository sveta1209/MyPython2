N = int(input())
member = []
for i in range(N):
    member.append(list(input().split()))
    member[i][1] = int(member[i][1])
    member[i][0], member[i][1] = member[i][1], member[i][0]
member.sort(reverse=True)
for i in range(N):
    print(member[i][1])
