input = [1,2,3,4,7]

result = []

def helper(S, pos,slate, sum, K):
    if sum > K:
        return
    if sum == K:
        result.append(slate[:])
        return True
    if pos == len(S):
        return
    
    helper(S, pos+1, slate, sum, K)
    slate.append(S[pos])
    helper(S, pos+1, slate, sum + S[pos], K)
    slate.pop()


helper(input, 0, [], 0,11)

print(result)















# def subsetsum(S,k):
#     return helper(S,0,k,[],0)

# def helper(s, pos, k, slate, sum):
#     if sum > k:
#         return 0
#     if sum == k:
#         return 1

#     if pos == len(s):
#         return 0
#     else:
#         return helper(s, pos+1, k, slate, sum) + helper(s, pos+1, k, slate + [s[pos]],sum+s[pos])


























# def find_something(array, pos, setsum, k , items=[]):
    
#     if pos == len(array):
#         if sum(setsum) == k:
#             items += setsum
#             return True
#         return 
#     else:
#         find_something(array, pos+1, setsum, k) #exclude
#         setsum += [array[pos]]
#         find_something(array, pos+1, setsum, k)#include
#         setsum.pop() 

#     return items

# input = [1,2,3,4,7]
# k = 11
# to_print = find_something(input, 0, [], k)

# print(to_print)



