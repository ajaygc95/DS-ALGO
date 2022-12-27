'''
=========================================================================
============================= Prim's Algorithm ==========================
=========================================================================

'''
import heapq

edges = [(0,1,4), (1,2,3),(0,2,2),(2,3,6)]
n = 4
adjlist = [ [] for _ in range(n)]

for src, dst, weight in edges:
    adjlist[src].append((dst, weight))
    adjlist[dst].append((src, weight))

captured = [-1]*n
source = 0 # source as second because of popping minimum wiehgt 
heap = [(0, source)]
total_dst  = 0

components = 0
while heap:
    weight, node = heapq.heappop(heap)
    if captured[node] != -1:
        continue
    captured[node] = 1 # mark visited as 1 not weight or anyting
    total_dst += weight
    components += 1

    if components == n:
        print(total_dst)
        break
    for nbr, wt in adjlist[node]:
        heapq.heappush(heap, (wt, nbr)) 

'''
Time complexity --> since there are multiple insertions and deletions.
                m edges --> m  insertions  + m deletions
                            O(logm)*m + O(logm)*m  --> heap implementation
                            2n(logm) --> n(logm) if sparse --> O(nlogm) same as kruskals
S(n) --> O(n) --> heap can go upto size order (n)
'''


    



