a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

eyes = int(input())
legs = int(input())
if eyes >= 8:
    if legs == 8:
        print("spider")
    else:
        print("scallop")
else:
    if legs == 10:
        print("bug")
    else:
        print("cat")
