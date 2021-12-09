H = int(input())
A = int(input())
B = int(input())
diff = A - B
print((H - A) // diff + ((H - A) % diff + diff - 1) // diff + 1)
