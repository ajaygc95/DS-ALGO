import heapq

given_list = [ 3,3, 1, 4, 4, 5, 2, 6, 1]

def frequentk(given_list):
    dict1 = {}

    for item in given_list:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1
    
    heap = [(value, key) for key, value in dict1.items()]
    largest = heapq.nlargest(2,heap)
    
    for i in range(2):
        print(largest[i])
       

frequentk(given_list)