#MERGE SORT(Divide and conquer)  ---> NOT IN PLACE
# Time Complexity is O(nlogn)

'''
function mergesrot(A):
    if length(A)<= 1: return
    mergeSort(A,?)


need helper funtion

function mergesorthelper(A, start, end):
    if start >= end : return

    mid = start + end//2

    mergersothelper(A,start, mid)
    mergersothelper(A,mid+1, end)

    i = start
    j = mid+1


'''


#QUICK SORT (Divide and Conquer) --- > In Place (No Auxilary Space)
#Lumoto's Partionting 
#In randomized QuickSort It is more likely that computer gets struck by lightning bolt thatn Quicksort running in o(n^2)

'''
QuickSort(A):
    if len(A)<=1:
        return
    Pick some x = A
'''

#TODO: Merge Sort is more stable thatn Quick Sort
#Abstract Data Typeddsss


#Priority Queues
#Binary HEAP

'''
    Priority of any node > = Prority of it's children

'''

#Heapify UP -- SWIM
#Heapify Down -- SINK
#Build HEAP
#Can be done in-place 
#Stability --> NO

"""
    Insert --> o(logn)
    Delete --> O(logn)
    Change Priority --> O(logn)
    Build head --> O(n)
"""
#QUICK SORT 
# HOARE PARTITION --> O( nlogn )
#Worst Case --> O(n^2)
# Average Case --> O(nlogn )

"""
Randomized and Algorithm
"""

# Decision Tree
# Counting Sort --> O(n) --> O(n+k) --> narrow (small constraint range example: Stuedents-age)
# 

'''Radix Sort''' #O(n) --> Linear Sort
# Counting sort with d-digit(3 digits is 245)
#Compare first place digit and second degit
# 345 is 5 and 4 and 3 and so on

#can do ONE INITIAL MSD -- DIvigin into 10 smaller pronlems

"""
Bucket Sort #LInease time
"""

