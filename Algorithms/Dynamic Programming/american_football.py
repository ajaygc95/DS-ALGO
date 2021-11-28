input = [2,3,6]
total = 8
globalbox = [0]

def helper(arr, slate,target):

    if target <0:
        return 
    
    if target == 0:
        globalbox[0] += 1
        return
    
    for item in input:

        helper(arr,slate+[item], target-item)
    

# def helper2(arr, target):





# helper(input, [], total)
# print(globalbox[0])

dptable = [0]*(total+1)
dptable[0] = 1

for i in range(len(dptable)):

    for score in input:

        if i-score >=0:
            dptable[i] += dptable[i-score]
    
print(dptable[-1])