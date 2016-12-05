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
    while i<10:
        listr=[]
        for k in range(1,10):
            if k!=j:
                if a[i][k]!=0:
                    listr.append(a[i][k])
        listc=[]
        for k in range(1,10):
            if k!=i:
                if a[k][j]!=0:
                    listc.append(a[k][j])
        listbox=listb.listb(a,i,j)
        listu=union.union3(listr,listc,listbox)
        listv=complement.complement(listu)
            
        if ((a[i][j]==0) or ([i,j] in listk)):
            if [i,j] not in listk:
                listk.append([i,j])
            k=a[i][j]+1
            while(k<10):
                print k
                err=errchk.errchk(k,listv)
                if err:
                    a[i][j]=k
                    j+=1
                    if j==10:
                        i+=1
                        j=1
                        break
                else:
                    k+=1
                    if (k==10):
                        a[i][j]=0
                        i=listk[-1][0]
                        j=listk[-1][0]
                        listk.pop(-1)
                        break
        else:
            j+=1
            if j==10:
                i+=1
                j=1
        output.output(a)
                
            
            
