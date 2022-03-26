input = [2,7,11,15]
target = 9

left = 0
right = len(input)-1

dict1 = {}

while left <= right:

    print(input[left])

    remaining = target - input[left]

    if input[left] in dict1:
        print(dict1[input[left]], left)
        break
    else:
        dict1[remaining] = left

    left += 1


# while left < right:

#     if input[left] + input[right]  < target:
#         left += 1
#     elif input[left] + input[right] > target:
#         right -=1 
#     else:
#         print(left, right)
#         break

