m__author__ = "Ajay GC"


items = [54,26,93,17,77,31,44,55,20]

for i in range(len(items)-1, 0,-1):
    for j in range(i):
        if items[i] < items[j]:
            items[j],items[i] = items[i], items[j]


print(items)