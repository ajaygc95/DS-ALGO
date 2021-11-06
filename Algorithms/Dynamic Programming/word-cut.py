input = "leetcode"
words = ["leet", "code"]



hmap = {}
for word in words:
    hmap[word] = 1

dptable = [False] * (len(input)+1)

for i in range(1,len(dptable)):

    dptable[i] = (input[:i] in hmap)

    for lastword in range(1,i):

        if input[i-lastword:i] in hmap and dptable[i-lastword] == True:
            dptable[i] = True

print(dptable) 
print(dptable[-1])