


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

        for col in range(n):

            



overall(4)