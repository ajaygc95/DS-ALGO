
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
        
        adjlist = [[] for _ in range(n)]
        
        for (s, d, w) in flights:
            adjlist[s].append((d,w))
              
        pq = [(0, 0, src)]
        
        while pq:
            (dist, level, node) = heapq.heappop(pq)
            
            if node == dst:
                return dist

            if level <= k:
                
                for (nbr, w ) in adjlist[node]:
                    heapq.heappush(pq,(dist+w, level+1, nbr))
        return -1
    
    # T(n) = O(  b^(K+1)  )