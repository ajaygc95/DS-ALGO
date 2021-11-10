


def overall(n):

    col = set()
    posDiag = set()
    negDiag = set()

    result = []
    board = [["-"]*n for i in range(n) ]

    def helper(pos):

        #base case:

        if pos == n:
            copy = ["".join(row) for row in board]
            result.append(copy)

            return 

        for c in range(n):

            if c in col or (pos+c) in posDiag or (pos-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(pos+c)
            negDiag.add(pos-c)

            board[pos][c] = "Q"
            helper(pos+1)
            
            col.remove(c)
            posDiag.remove(pos+c)
            negDiag.remove(pos-c)
            board[pos][c] = "-"


    helper(0)

    return result


store = overall(4)
print(store)