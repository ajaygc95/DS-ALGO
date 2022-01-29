input = "226"

def numDecodings(self, input: str) -> int:
    dptable = [0]*(len(input)+1)

    dptable[0] = 1
    dptable[1] = 1 if input[0] != "0" else 0

    # print(dptable)
    
    six1 = ["0","1","2","3","4","5","6"]
    
    for i in range(2, len(dptable)):
        # print("running", input[i-1])
        # print(dptable)
        
        if input[i-1] != "0":
            dptable[i] += dptable[i-1]

        if input[i-2] == "1" or (input[i-2] =="2" and input[i-1] in six1) :
            # print("found", input[i-2])
            dptable[i] += dptable[i-2]
            
    # print(dptable)
    return dptable[-1]


