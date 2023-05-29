nums = [1,2,3,3,5]
target = 6
left_pointer = 0
right_pointer = 0

end = len(nums)-1

result = []

running_count = 0
while right_pointer <= end:
    print("========================")
    print(f"adding {nums[right_pointer]} to {running_count}")
    running_count += nums[right_pointer]

    print(nums[right_pointer], running_count)
    if running_count == target:
        result.append(nums[left_pointer:right_pointer+1])


    while running_count >= target and left_pointer <= right_pointer:
        print(f"subtracting {nums[left_pointer]} from {running_count}")

        running_count -= nums[left_pointer]
        left_pointer += 1
        if running_count == target:
            result.append(nums[left_pointer:right_pointer+1])

    right_pointer += 1

print(result)

