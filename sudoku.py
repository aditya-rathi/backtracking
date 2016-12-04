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
        if a[i][j]==0 or ([i,j] in listk):
            if [i,j] not in listk:
                listk.append([i,j])
            a[i][j]=1
            while a[i][j]<11:
                error=errchk.errchk(a[i][j],listv)
                if error:
                    a[i][j]+=1
                    if a[i][j]==10:
                        a[i][j]=0
                        j=listk[len(listk)-1][1]
                        i=listk[len(listk)-1][0]
                        listk.pop(-1)
                        a[i][j]+=1
                        break
                else:
                    j+=1
                    if j==10:
                        j=1
                        i+=1
                    break

        else:
            j+=1
            if j==10:
                j=1
                i+=1
            

        output.output(a)
            
            
