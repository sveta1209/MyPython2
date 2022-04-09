fin = open('input.txt', 'r', encoding='utf8')
#a = int(fin.readline())
#b = int(fin.readline())
#for line in fin:
#c = fin.readlines()
   # print(line)
#print(a+b)
fout = open('output.txt', 'w', encoding='utf8')
print(sum(map(int, fin.readlines())), file=fout)
