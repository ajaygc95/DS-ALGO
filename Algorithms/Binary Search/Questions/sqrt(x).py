# import math
# # print(math.sqrt(8))
# x = 4

# def sqrt(x):
#     if x < 2:
#         return x
    
#     left, right = 0, x 
    
#     while left <= right:
#         pivot = (left+right)// 2
#         num = pivot * pivot
#         if num > x:
#             right = pivot -1
#         elif num < x:
#             left = pivot + 1
#         else:return pivot
        
#     return right
    
# print(sqrt(8))



# def sqrt(x):
#     start = 0 
#     end = x
#     if x < 1:
#         start = 0.25
#         end = 1

#     while start <= end:
#         mid = (start+end)/2
#         if x-0.001 <= mid**2 <= x+0.001:
#             return mid
#         elif mid**2 < x:
#             start = mid+0.001
#         else:
#             end -= 0.001
#     return None

# print(round(sqrt(8),3))

dptable = [0]*10

for i in range(10):
    dptable[i] = 1

print(dptable)