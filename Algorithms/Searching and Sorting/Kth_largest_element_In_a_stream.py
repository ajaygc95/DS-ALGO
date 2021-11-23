import heapq


def kth_largest(k, initial_stream, append_stream):

    heap = initial_stream

    heapq.heapify(heap)


    for _ in range(len(heap)-k):
        heapq.heappop(heap)
    
    print(heap)

    values = []


    for i in append_stream:

        if len(heap)<k:
            heapq.heappush(heap,i)
        else:
            if i > heap[0]:
                heapq.heappushpop(heap,i)
        
        values.append(heap[0])


    return values





    

print(kth_largest( 2, [4,6], [5,2,20]))



    


    
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