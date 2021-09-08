given_list = [[1, 5], [5, 8], [10, 15]]

def possible(given_list):
    given_list.sort()
    last_end = -1

    for start, end in given_list:
        print(last_end, start)
        if last_end <= start:
            last_end = end
        else:
            return False
    return True


yse  = possible(given_list)
print(yse)