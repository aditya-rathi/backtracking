def input1(name):
    f=open(name)
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].strip()
        lst[i]=lst[i].split("\t")
    d={}
    for i in range(len(lst)):
        if i+1 not in d:
            d[i+1]={}
        for j in range(len(lst[i])):
            d[i+1][j+1]=lst[i][j]
            d[i+1][j+1]=int(d[i+1][j+1])
    return d

    
    
