
import heapq
input = [3, 8, 5, 2]

heap = []

heapq.heapify(heap)


values = []
sum = 0
for i in input:

    heapq.heappush(heap,i)



    print(heap)

    

    mid = len(heap)%2
    median = len(heap)//2
    if len(heap)<1:
        values.append(heap[0])

      
    else:
        value = (heap[median-1] + heap[median])//2

        if mid == 1:
            # print(heap[median])
            values.append(heap[median-1])
        else:
            # print(heap[median-1], heap[median])
            values.append(value)



# print(values)

