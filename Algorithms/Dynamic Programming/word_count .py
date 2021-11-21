txt = "kickstartisawesome"
dict =  ["kick", "start", "kickstart", "is", "awe", "some", "awesome"]


dptable = [False] *(len(txt)+1)

dptable[0] = True


for i in range(1, len(dptable)):

    for lastword in range(i):

        if dptable[i-lastword-1] and txt[i-lastword-1:i] in dict:
            dptable[i] = True


print(dptable)


