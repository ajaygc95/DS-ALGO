
#Find all combination with 3 choices that can be painted with 2 colors and only two adjcent fence 
# can be printed same

n = 3
k = 2

total = [0]*n
same = [0]*n
diff = [0]*n



same[0] = 0
diff[0] = k
total[0] = k

print(total)
print(diff)
print(same)

for i in range(1, n):
    same[i] = diff[i-1]
    diff[i] = total[i-1]*(k-1)
    total[i] = same[i] + diff[i]

print(total[-1])

