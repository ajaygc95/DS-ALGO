from collections import deque


input = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,0],
    [0,1,0,1,0]
]


def overall(input):
    count = 0

    def getNbr(row, col):

        result = []

        if row-1 >= 0:
            result.append((row-1,col))

        if col-1 >= 0:
            result.append((row,col-1))

        if row+1 < len(input):
            result.append((row+1, col))

        if col+1 <len(input[0]):
            result.append((row,col+1))
        return result


    def helper(i,j):

        input[i][j] = 2
        q = deque()
        q.append((i,j))
        for item in input:
            print(item)
        while q:

            (row, col) = q.popleft()
            nbr = getNbr(row,col)

            for (i,j) in nbr:
                if input[i][j] == 1:
                    input[i][j] = 2
                    q.append((i,j))


    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 1:
                helper(i,j)
                count += 1
    return count


store = overall(input)

print(store)


















# count = 0
# def getNbr(row, col):
#     print("======" )
#     print(row,col)
#     print("count:", count)

#     if row < 0 or row >= len(input) or col < 0 or col > len(input[0]) or input[row][col] != 1:
#         print("returned")
#         return
    
#     input[row][col] = 2

#     getNbr(row-1, col)
#     getNbr(row+1,col)
#     getNbr(row, col-1)
#     getNbr(row, col+1)
    

# for i in range(len(input)):
#     for j in range(len(input[0])):

#         if input[i][j] == 1:
#             print("one found", i,j)
#             getNbr(i,j)
#             count += 1
#         print()

# print(count)