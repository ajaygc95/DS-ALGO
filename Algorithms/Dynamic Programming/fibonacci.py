input = 20

memoize = [0]* 3
memoize[0] = 0
memoize[1] = 1

def helper(n):

    for i in range(2,n+1):
        memoize[i%3] = memoize[(i-1)%3] + memoize[(i-2)%3]


helper(input)
print(memoize)
print(len(memoize))



