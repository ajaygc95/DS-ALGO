height = [1,8,6,2,5,4,8,3,7]

rest = 0

# for l in range(len(height)):
#     for r in range(l+1, len(height)):
#         area = (r-l)*min(height[l],height[r])
#         rest = max(rest,area)
l = 0
r = len(height) -1

while l <= r:
    rest = max(rest, min(height[l],height[r])*(r-l))
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1






print(rest)