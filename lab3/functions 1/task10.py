a=["ef",0,0,5,7,2,2,3,4,"ef",34,"efdwef","wef","wef",34]
b=[]
def unique(a):
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
unique(a)