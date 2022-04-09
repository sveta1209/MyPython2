S, N = list(map(int, input().split()))
new_list = []
for i in range(N):
    new_list.append(int(input()))
new_list.sort()
while sum(new_list) > S:
    new_list.pop()
print(len(new_list))
