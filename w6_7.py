fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
a = []
for line in fin:
    a.append(line.split())
a.sort()
for i in range(len(a)):
    print(a[i][0], a[i][1], a[i][3], file=fout)
fin.close()
fout.close()
