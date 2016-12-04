import input1
import output
import union
import listb
import complement

def sudoku(name):
    a=input1.input1(name)
    c={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    while (c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+c[9]<81):
        for i in range(1,10):
            if c[i]<9:
                c[i]=0
                for j in range(1,10):
                    if a[i][j]!=0:
                        c[i]+=1
                    else:
                        listr=[]
                        for k in range(1,10):
                            if a[i][k]!=0:
                                listr.append(a[i][k])
                        listc=[]
                        for k in range(1,10):
                            if a[k][j]!=0:
                                listc.append(a[k][j])
                        listbox=listb.listb(a,i,j)
                        listu=union.union3(listr,listc,listbox)
                        listu.sort()
                        
                        
