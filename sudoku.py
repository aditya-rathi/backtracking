import input1
import output
import union
import listb
import complement

def sudoku(name):
    a=input1.input1(name)
    while (c<81):
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
            
            
