input = ["cat", "hat", "bad", "had"]
start = "bat"
stop = "had"





adj_list = [[0]*len(input[0]) for _ in range(len(input))]

for i in range(len(input)):
    for j in range(len(input[0])):
        adj_list[i][j] = input[i][j]


