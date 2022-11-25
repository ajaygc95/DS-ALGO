n = 4
board =  [["."]*n for _ in range(n)]

for item in board:
    print(item)

visited = set()

res = []

cols = set()
posDiag = set()
negDiag = set()


def helper(row, board):
    if row == n:
        copy = [''.join(each_row) for each_row in board]
        res.append(copy)
        return 

    for col in range(n):

        if col in cols or (row+col) in posDiag or (row-col) in negDiag:
            continue
        cols.add(col)
        posDiag.add(row+col)
        negDiag.add(row-col)
        board[row][col] = "Q"

        helper(row+1, board)
        
        board[row][col] = "."
        posDiag.remove(row+col)
        negDiag.remove(row-col)

helper(0, board)
print(res)



    
    


        

    
        

    
