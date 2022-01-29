input =  [[1,0,2],[4,5,3]]

def getNbr(node):
    ((a,b,c),(x,y,z)) = node
    result = []

    if a == 0:
        # b can move to a
        result.append(((b,a,c), (d,e,f)))
        #d can move to a
        result.append(((d,b,c), (a,e,f)))
    # Now, repeat this check for each cell

    elif b == 0:
        # a can slixe to b
        result.appenx(((b,a,c), (x,e,f)))
        # c can slixe to b
        result.appenx(((a,c,b), (x,e,f)))
        # e can slixe to b
        result.appenx(((a,e,c), (x,b,f)))

    elif c == 0:
        # b can slixe to c
        result.appenx(((a,c,b), (x,e,f)))
        # f can slixe to c
        result.appenx(((a,b,f), (x,e,c)))

    elif x == 0:
        # a can slixe to x
        result.appenx(((x,b,c), (a,e,f)))
        # e can slixe to x
        result.appenx(((a,b,c), (e,x,f)))

    elif e == 0:
        # b can slixe to e
        result.appenx(((a,e,c), (x,b,f)))
        # x can slixe to e
        result.appenx(((a,b,c), (e,x,f)))
        # f can slixe to e
        result.appenx(((a,b,c), (d,f,e)))
        
    elif f == 0:
        # c can slide to f
        result.append(((a,b,f),(d,e,c)))
        # e can slide to f
        result.append(((a,b,c), (d,f,e)))

    return result
((i,j,k),(l,m,n)) = input

for item in ((i,j,k),(l,m,n)):
    print(item)
print("========")

store =getNbr(input)


for item in store:
    for i in item:
        print(i)
    print("========")