lists=[1,3],[5,6]
def merge(*lists):
    b=sum(lists,[])
    b.sort()
    print (b)
merge(*lists)
