n = 5
for x in range(1,n+1):
    s = n-x
    for y in range(1,n+1):
        print(chr(s+65)+"", end=' ')
        s=s+n
    print()