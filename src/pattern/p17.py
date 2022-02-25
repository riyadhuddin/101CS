for x in range(1,10):
    for y in range(1,x+1):
        print('%s/%s=%s \n'%(y,x,y/x),end='\t')
    print()