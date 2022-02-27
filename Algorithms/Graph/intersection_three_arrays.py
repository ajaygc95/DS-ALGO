arr1 = [2, 5, 10]

arr2 = [2, 3, 4, 10]

arr3 = [2, 4, 10]


final_arr = []


i = j = k = 0


while i < len(arr1) and j < len(arr2) and k < len(arr3):
    print(i,j,k)

    if arr1[i] == arr2[j] and arr2[i] == arr3[k]:
        final_arr.append(arr1[i])
        i += 1
        j += 1 
        k += 1
    
    if arr1[i] < arr2[j]:
        i += 1
    # elif arr1[j] < arr3[k]:
        j += 1
    else: 
        k += 1
    
print(final_arr)