import heapq
edges = [[1,2,2],[1,3,1],[2,5,2],[5,4,2],[3,4,1]]
n, source, dst = 5,1,4
adjlist = [[] for _ in range(n+1)]

for src, dst, weight in edges:
    adjlist[src].append((dst, weight))

captured = [-1]*(n+1)
priority_queue = [(0, source)]
count_node = 0
last_dist = 0

while priority_queue:
    distance, node = heapq.heappop(priority_queue)
    if captured[node] != -1:
        continue
    
    captured[node] = distance
    count_node += 1
    last_dist = distance

    if count_node == n:
        print(last_dist)
        break
    for nbr, nbr_wt in adjlist[node]:
        heapq.heappush(priority_queue, (nbr_wt+captured[node], nbr))

'''
Time Complexity
mlogm --> nlogn for sparse graph
'''







class Solution:
    def smallestSubsequence(self, s: str) -> str:

        hash_map = collections.Counter(s)
        stack = []

        for character in s:

            hash_map[character] -= 1
   
            if stack and character < stack[-1]:
                while stack and character < stack[-1] and hash_map[stack[-1]] > 0 and   character not in stack:
                    stack.pop()
            if character not in stack:
                stack.append(character)

        return ''.join(stack)