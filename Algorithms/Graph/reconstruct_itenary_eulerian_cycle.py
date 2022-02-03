
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
def findItinerary(tickets):
    
    tickets.sort(reverse=True)
    adjlist = {}
    
    for src, dest in tickets:
        if src not in adjlist:
            adjlist[src] = []
        if dest not in adjlist:
            adjlist[dest] = []
        adjlist[src].append(dest)
        
    result = []
    
    def helper(node):
        
        while len(adjlist[node]) > 0:
            
            nbr = adjlist[node].pop()
            helper(nbr)
        
        result.append(node)
        
    helper("JFK")

    return result[::-1]

store = findItinerary(tickets)
print(store)