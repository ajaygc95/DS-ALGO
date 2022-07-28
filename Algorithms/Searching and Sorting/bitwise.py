from turtle import textinput


a = 20 
b = 30

while b != 0:
    tmp = (a&b)<<1
    a = a^b
    b =tmp

print(a)



