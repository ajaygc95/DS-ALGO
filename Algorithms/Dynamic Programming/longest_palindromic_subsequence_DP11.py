class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dptable = [[0]*(len(s)) for _ in range(len(s))]
                
        for row in range(len(dptable)):
            dptable[row][row] = 1
          
        for row in range(len(dptable), -1, -1):
            for col in range(row+1, len(dptable)):
                
                if s[row] == s[col]:
                    dptable[row][col] = dptable[row+1][col-1] + 2
                else:
                    dptable[row][col] = max( dptable[row+1][col], dptable[row][col-1])
                               
        # for item in dptable:
        #     print(item)
        
        return dptable[0][-1]
    
    # T(N) == O(n^2)
    # S(N) == O(n^2) can be saved by using only two rows O(1)