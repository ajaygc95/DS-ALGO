txt = "kickstartisawesome"
dict =  ["kick", "start", "kickstart", "is", "awe", "some", "awesome"]


dptable = [-1] *(len(txt)+1)

dptable[0] = [1]


for i in range(1, len(dptable)):

    for lastword in range(1,i):
        if dptable[i]

