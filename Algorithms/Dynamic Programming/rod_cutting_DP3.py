from tkinter import N


price = [1,3,5,6,9]
n = 4


dptable = [0]*n 

dptable[0] = 0
dptable[1] = price[0]

for i in range(2, n):

    for j in range(1, i):

        dptable[i]  = max(price[j] + dptable[i-j],dptable[i])

print(dptable[i])