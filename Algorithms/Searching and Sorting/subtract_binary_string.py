a = "1101"
b = "101"

def binary_difference(a, b):
    num1 = a[::-1]
    num2 = b[::-1]
    carry = 0
    res = ""
    for index in range(len(a)):
        value1 = int(num1[index])
        value2 = int(num2[index]) if index < len(num2) else 0
        res += str(total)
    return res[::-1]

return_value = binary_difference(a, b)
print(return_value)








