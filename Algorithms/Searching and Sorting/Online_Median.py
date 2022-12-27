
import heapq
def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    
    left = [] # max_heap
    right = [] # min_heap

    
    def insert(item):
        print(left, right)
        if len(left) <= len(right):
            print(f"{item} in left")
            if right and item > right[0]:
                pop_value = heapq.heappop(right)
                heapq.heappush(right, item)
                heapq.heappush(left, -pop_value)
                
            else:
                heapq.heappush(left, -item)
                
        else:
            if left and item < -left[0]:
                pop_value = heapq.heappop(left)
                heapq.heappush(left, -item)
                heapq.heappush(right, -pop_value)
            else:
                heapq.heappush(right, item)
            
    result = []    
    for item in stream:
        insert(item)
        
        if len(left) == len(right):
            result.append((-left[0]+right[0])//2)
        else:
            result.append(-left[0])
    # return result

    print(result)

online_median([3,8,5,2])














































# import heapq
# from turtle import st
# stream = [1,2,3,4,5]

# left = []
# right = [8,9,10]


# heapq._heapify_max(right)
# yes = heapq.heappop(right)

# print(yes)
# heapq._heapify_max(left)
# heapq.heapify(right)

# values = []

# def valid(left, right):

#     if left[0] > right[0]:
#         lefti = heapq._heappop_max(left)
#         righti = heapq.heappop(right)

#         heapq.heappush(right,lefti)
#         heapq.heappush(left, righti)
#         heapq._heapify_max(left)


# for i in stream:
#     heapq.heappush(left, i)
#     heapq._heapify_max(left)



#     if left and right:
#         valid(left, right)

#     if len(left) - len(right)>1:
#         item = heapq._heappop_max(left)
#         heapq.heappush(right,item)

#         valid(left, right)
    
#     if len(right)-len(left)>1:
#         item = heapq.heappop(right)
#         heapq.heappush(left,i)
#         heapq._heapify_max(left)
#         valid(left, right)

#     if len(right) > len(left):
#         values.append(right[0])
    
#     elif len(left)> len(right):
#         values.append(left[0])
    
#     else:
#         values.append((left[0]+right[0])//2)

#     print(left,right)


# print(values)









# # for i in input:

# #     heapq.heappush(left,i)
# #     heapq._heapify_max(left)

# #     if len(left) - len(right)>1:
# #         item = heapq._heappop_max(left)
# #         heapq.heappush(right,item)

# #         valid(left, right)
    
# #     if len(right)-len(left)>1:
# #         item = heapq.heappop(right)
# #         heapq.heappush(left,i)
# #         heapq._heapify_max(left)
# #         valid(left, right)
    


# #     if len(right) > len(left):
# #         values.append(right[0])
    
# #     elif len(left)> len(right):
# #         values.append(left[0])
    
# #     else:
# #         values.append((left[0]+right[0])//2)


# #     print(left,right)
# # print(values)

#     # if abs(len(left) - len(right)) == 1 or abs(len(left) - len(right))==0 :

#     #     heapq.heappush(left,i)
#     #     heapq._heapify_max(left)

#     #     if len(left)-len(right)>1:

#     #         item = heapq._heappop_max(left)
#     #         print("item :", item)
#     #         heapq.heappush(right, item)
        
#     #     if len(left)>len(right):
#     #         values.append(left[0])
#     #     elif len(right)>len(left):
#     #         values.append(right[0])

#     #     else:
#     #         values.append((left[0]+right[0])//2)


# # print(left, right)
# # print(values)





















# # for i in input:

# #     heapq.heappush(heap,i)

# #     print(heap)

# #     mid = len(heap)%2
# #     median = len(heap)//2
# #     if len(heap)<1:
# #         values.append(heap[0])

      
# #     else:
# #         value = (heap[median-1] + heap[median])//2

# #         if mid == 1:
# #             # print(heap[median])
# #             values.append(heap[median-1])
# #         else:
# #             # print(heap[median-1], heap[median])
# #             values.append(value)



# # # print(values)

