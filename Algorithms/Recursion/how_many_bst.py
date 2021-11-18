def swap(a,b,array):
    array[a], array[b]  = array[b], array[a]

globalbox = [0]
def how_many_bst(n, i=-1):
    print(globalbox)
    if n == 1 or n == 0:
        globalbox[0] += 1
        return 

    how_many_bst(n-1)* how_many_bst(i+1)

input = 5
to_print = how_many_bst(input)
print(to_print)