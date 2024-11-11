def chop(lst) :
    lstlen=len(lst)
    del(lst[lstlen-1])
    del(lst[0])
    return None

def middle(lst) :
    lstlen=len(lst)
    del(lst[lstlen-1])
    del(lst[0])
    return lst

lst=[1,2,3,4,5,6]
newlst=middle(lst)
print(newlst)
