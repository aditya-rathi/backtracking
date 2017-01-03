import input1
import output
import union
import listb
import complement
import errchk

def sudoku(name):
    global listk
    a=input1.input1(name)
    i=1
    j=1
    listk=[]
    for i in a:
        for j in a[i]:
            if a[i][j]==0:
                listk.append([i,j])
    u=0
    print listk[u][0]
    while u<len(listk):
        listr=[]
        listbox=[]
        listc=[]
        x=listk[u][0]
        y=listk[u][1]
        for k in range(1,10):
            if a[x][k]!=0:
                listr.append(a[x][k])
            if a[k][y]!=0:
                listc.append(a[k][y])
        listbox=listb.listb(a,x,y)
        listu=union.union3(listr,listc,listbox)
        listv=complement.complement(listu)
        a[x][y]+=1
        while a[x][y]<=10:
            error=errchk.errchk(a[x][y],listv)
            if error:
                a[x][y]+=1
            else:
                u+=1
                x=listk[u][0]
                y=listk[u][1]
                break
                    
        if a[x][y]==11:
            a[x][y]=0
            u-=1
        
            
    output.output(a)
            
            
