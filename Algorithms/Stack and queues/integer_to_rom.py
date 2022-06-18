
nums = 58


symlist = [ 
    ("I", 1),
    ("IV", 5),
    ("IX", 9),
    ("X", 10),
    ("XL", 40),
    ("V", 50),
    ("XC", 90),
    ("C", 100),
    ("CD", 400),
    ("D", 500),
    ("CM", 900),
    ("M", 1000),

]

res = ""

for rom, integer in reversed(symlist):
    calc = nums//integer
    if  calc>=0:
        res += rom*calc
        nums = nums%integer
    
    if nums == 0:
        break

print(res)


