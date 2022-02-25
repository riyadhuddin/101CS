n = 10
s = 1
for x in range(1,n+1):
    for y in range(1,n+1):
        print(")", end=' ')
        print(x, end=' ')
        print(y, end=' ')
        print(s, end=' ')
        s+=1
    print()