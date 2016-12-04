def output(a):
    o={10:'+-----------------------------+',1:'| ',11:'|        |        |           |',2:'| ',21:'|        |        |           |',3:'| ',31:'|        |        |           |',4:'| ',41:'|        |        |           |',5:'| ',51:'|        |        |           |',6:'| ',61:'|        |        |           |',7:'| ',71:'|        |        |           |',8:'| ',81:'|        |        |           |',9:'| ',91:'+-----------------------------+'}
    oline=[]
    for i in range(1,10):
        for j in range(1,10):
            if (j==3 or j==6 or j==9):
                o[i]=o[i]+str(a[i][j])+' | '
            else:
                o[i]=o[i]+str(a[i][j])+"  "
    oline.append(o[10])
    for i in range(1,10):
        oline.append(o[i])
        k=i*10+1
        oline.append(o[k])
    for i in oline:
        print i
    
