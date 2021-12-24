number = 23
x = 2
result = ""

while number >= x:
    quotient = number//x
    remainder = number%x
    result += str(remainder)
    number = quotient

result += str(number)

print(result[::-1])

