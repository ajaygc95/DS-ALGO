given_list =[1, 4, 3, 5, 10]
target = 7

def pair_sum_sorted_array(numbers, target):

    start = 0
    right =  len(numbers)-1

    while start <= right:

        if numbers[start] + numbers[right] == target:
            return [start,right]

        if numbers[start] + numbers[right] > target:
            right -= 1
        else:
            start += 1

print(pair_sum_sorted_array(given_list,target))
