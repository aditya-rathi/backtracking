def union3(lst1,lst2,lst3):
    lst4=[]
    for i in lst1:
        lst4.append(i)
    for i in lst2:
        if i not in lst4:
            lst4.append(i)
    for i in lst3:
        if i not in lst4:
            lst4.append(i)
    return lst4

