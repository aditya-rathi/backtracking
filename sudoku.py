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
    i=1
    j=1
    while i<10:
        listr=[]
        listbox=[]
        listc=[]
        for k in range(1,10):
            if a[i][k]!=0:
                listr.append(a[i][k])
            if a[k][j]!=0:
                listc.append(a[k][j])
        listbox=listb.listb(a,i,j)
        listu=union.union3(listr,listc,listbox)
        listv=complement.complement(listu)
        if ([i,j] in listk):
            a[i][j]+=1
            while a[i][j]<=10:
                error=errchk.errchk(a[i][j],listv)
                if error:
                    a[i][j]+=1
                else:
                    j+=1
                    if j==10:
                        j=1
                        i+=1
                    break
                    
            if i<10 and j<10:
                if a[i][j]==11:
                    a[i][j]=0
                    c=listk.index([i,j])
                    i=listk[c-1][0]
                    j=listk[c-1][1]
            
        else:
            j+=1
            if j==10:
                j=1
                i+=1
            
    output.output(a)
            
            
