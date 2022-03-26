# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1,0]

left = 0
right = len(prices)-1
minLeft = prices[0]
maxRight = prices[-1]

while left <= right:
    print(minLeft, maxRight)
    if prices[left] < minLeft:
        minLeft = prices[left]
    
    if prices[right] > maxRight:
        maxRight = prices[right]    
    
    left += 1
    right -=1 

result = maxRight - minLeft
result if result >=0 else 0

print(result)