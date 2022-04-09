fin = open('input.txt', 'r', encoding='utf8')
K = int(fin.readline())
new_list = []
for a in fin:
    a_splt = a.split()
    po1 = int(a_splt[-3])
    po2 = int(a_splt[-2])
    po3 = int(a_splt[-1])
    if po1 >= 40 and po2 >= 40 and po3 >= 40:
        new_list.append(po1 + po2 + po3)
fin.close()

new_list.sort(reverse=True)

if len(new_list) <= K:
    print(0)
else:
    if new_list[K - 1] == new_list[K]:
        d = K - 1
        while d > 0 and new_list[d - 1] == new_list[d]:
            d = d - 1
        if d == 0:
            print(1)
        else:
            print(new_list[d - 1])
    else:
        print(new_list[K - 1])
