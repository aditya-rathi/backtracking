def listb(a,i,j):
    lst=[]
    if((i-1)%3==0):
        if((j-1)%3==0):
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        elif((j-2)%3==0):
            for k in range(i,i+3):
                for l in range(j-1,j+2):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        else:
            for k in range(i,i+3):
                for l in range(j-2,j+1):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
    elif((i-2)%3==0):
        if((j-1)%3==0):
            for k in range(i-1,i+2):
                for l in range(j,j+3):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        elif((j-2)%3==0):
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        else:
            for k in range(i-1,i+2):
                for l in range(j-2,j+1):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
    else:
        if((j-1)%3==0):
            for k in range(i-2,i+1):
                for l in range(j,j+3):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        elif((j-2)%3==0):
            for k in range(i-2,i+1):
                for l in range(j-1,j+2):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
        else:
            for k in range(i-2,i+1):
                for l in range(j-2,j+1):
                    if a[k][l]!=0:
                        lst.append(a[k][l])
    return lst
        
