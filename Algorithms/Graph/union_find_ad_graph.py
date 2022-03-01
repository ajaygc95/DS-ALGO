edges = None

component = None#something

def find(x):
    curr = x 
    while component[curr] != curr:
        curr = component[curr]
    return curr

for u, v in edges:
    lu = find(u)
    lv = find(v)
    if lu != lv:
#         component[v] = component[u]
    


# Learned Instagram today. 

