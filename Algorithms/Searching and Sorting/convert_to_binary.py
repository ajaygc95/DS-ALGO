digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

number = 125
x = 64
result = ""

h_map = {}

while number >= x:
    quotient = number//x
    remainder = number%x
    result += str(digits[remainder])
    number = quotient

if number > 0:
    result += str(digits[number])

decoded = result[::-1]
initial = "https://bit-ly/" 
final = initial + decoded
print(final)
