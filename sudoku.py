import input1
import output
import union
import listb
import complement

def sudoku(name):
    a=input1.input1(name)
    i=1
    j=1
    while i<10 and j<10:
        listr=[]
        listbox=[]
        listc=[]
        for k in range(1,10):
            listr=a[i][k]
            listc=a[k][j]
        listbox=listb.listb(a,i,j)
        listu=union.union3(listr,listc,listbox)
        listu.sort()
        listv=complement.complement(listu)
        if a[i][j]==0:
            a[i][j]=1
            #errorcheck
            if error:
                a[i][j]+=1
                if a[i][j]==10:
                    a[i][j]=0
                    j=j-1
                    if j==0:
                        j=9
                        i=i-1

        else:
            i+=1
            j+=1
            
            
            
