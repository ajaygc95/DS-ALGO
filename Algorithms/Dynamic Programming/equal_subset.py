n=6


input = [10, -3, 7, 2, 1, 3]


# There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:

# s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)
# s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]
# s1 = [10] and s2 = [-3, 3, 7, 2, 1]
# s1 = [-3, 3, 7, 2, 1] and s2 = [10]
# s1 = [10, -3, 2, 1] and s2 = [7, 3]
# s1 = [7, 3] and s2 = [10, -3, 2, 1]


sum = sum(input)

dptable =[0]*(sum+1)

dptable[0] = 0

for i in range(dptable):
    count1 = 0
    count2 = 0
    for item in input:
        count1 = input[i]


