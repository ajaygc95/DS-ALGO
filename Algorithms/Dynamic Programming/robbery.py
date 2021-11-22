values = [2,8]
dptable = [0]*(1+len(values))

dptable[1] = values[0]
dptable[2] = values[1]
keeper = 0

print(dptable)

for i in range(2,len(dptable)):
    
    dptable[i] = max(dptable[i-2], dptable[i-3]) + values[i-1]
    


print(dptable)