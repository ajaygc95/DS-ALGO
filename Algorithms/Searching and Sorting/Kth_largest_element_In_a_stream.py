
import heapq
input1 = [4,6]
input2 = [5,2,20]
k = 2



def helper(k, first_stream, second_stream):
    left = first_stream

    heapq.heapify(left)

    for i in range(len(left)-k):
        heapq.heappop(left)
    values= []
    for i in second_stream:

        if len(left)<k:
            heapq.heappush(left,i)
        else:
            if i > left[0]:
                heapq.heappushpop(left,i)
        
        values.append(left[0])


    return values

store = helper(k,input1, input2)
print(store)



















# import heapq


# def kth_largest(k, initial_stream, append_stream):

#     heap = initial_stream

#     heapq.heapify(heap)


#     for _ in range(len(heap)-k):
#         heapq.heappop(heap)
    
#     print(heap)

#     values = []


#     for i in append_stream:

#         if len(heap)<k:
#             heapq.heappush(heap,i)
#         else:
#             if i > heap[0]:
#                 heapq.heappushpop(heap,i)
        
#         values.append(heap[0])


#     return values

# print(kth_largest( 2, [4,6], [5,2,20]))



    


    
    # for i in range(len(heap)-k):
    #     heapq.heappop(heap)


    # heap = initial_stream
    # heapq.heapify(heap)

    # for i in range(len(heap)-k):
    #     heapq.heappop(heap)
    # values = []

    # for i in append_stream:
    #     if len(heap) < k:
    #         heapq.heappush(heap, i)
    #     elif i > heap[0]:
    #         heapq.heappushpop(heap, i)

    #     values.append(heap[0])

    # return values