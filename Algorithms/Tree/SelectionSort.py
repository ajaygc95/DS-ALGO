__author__ = "Ajay GC"

items = [54,26,93,17,77,31,44,55,20]

for i in range(len(items)-1, 0, -1):
    position = 0
    for j in range(1,i+1):
        if items[j] > items[position]:
            position = j

    items[j],items[position] = items[position],items[j]

print(items)