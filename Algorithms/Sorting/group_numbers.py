given_list = [3,1,2,5]

def swap(a,b,arr):
    arr[a],arr[b] = arr[b], arr[a]

def solve(arr):
    i = 0
    j = len(arr)-1

    while i <= j:
        if arr[i]%2 ==0:
            i += 1
        else:
            if arr[j]%2 == 0:
                swap(i,j,arr)
                j -=1 
            else:
                j -= 1
        

solve(given_list)
print(given_list)