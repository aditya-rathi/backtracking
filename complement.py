def complement(lst):
    lst1=[1,2,3,4,5,6,7,8,9]
    lst2=[]
    for i in lst1:
        if i not in lst:
            lst2.append(i)
    return lst2

        
