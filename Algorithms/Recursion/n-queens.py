


def overall(n):

    col = set()
    posDiag = set()
    negDiag = set()
    globalbox = []

    board = [["."]*(n) for _ in range(n)]

    def helper(pos):
        if pos == n:
            copy = [''.join(row) for row in board]
            globalbox.append(copy)

            return 

        for item in range(n):


            if item in col or (pos + item) in posDiag or (pos-item) in negDiag:
                continue
                
            col.add(item)
            posDiag.add(pos+item)
            negDiag.add(pos-item)
            board[pos][item] = "Q"

            helper(pos+1)

            col.remove(item)
            posDiag.remove(item+pos)
            negDiag.remove(pos-item)
            board[pos][item] = "."

    helper(0)
    return globalbox




store =overall(4)
print(store)




















# def overall(n):

#     col = set()
#     posDiag = set()
#     negDiag = set()

#     result = []
#     board = [["-"]*n for i in range(n) ]

#     def helper(pos):

#         #base case:

#         if pos == n:
#             copy = ["".join(row) for row in board]
#             result.append(copy)

#             return 

#         for c in range(n):

#             if c in col or (pos+c) in posDiag or (pos-c) in negDiag:
#                 continue

#             col.add(c)
#             posDiag.add(pos+c)
#             negDiag.add(pos-c)

#             board[pos][c] = "Q"
#             helper(pos+1)
            
#             col.remove(c)
#             posDiag.remove(pos+c)
#             negDiag.remove(pos-c)
#             board[pos][c] = "-"


#     helper(0)

#     return result


# store = overall(4)
# for item in store:
#     print(item)