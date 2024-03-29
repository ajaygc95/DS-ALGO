# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1 = "aabaac"
s2 = "aadaaeaaf"
s3 = "aadaaeaabaafaac"

len1, len2 , len3 = len(s1), len(s2), len(s3)

# if len1 + len2 != len3:
#     return False

# if len1 == 0:
#     return s2 == s3
# if len2 == 0:
#     return s1 == s3

dptable = [[False]*(len(s1)+1) for _ in range(len(s2)+1)]

dptable[0][0] = True

for col in range(1, len(dptable[0])):
    dptable[0][col] = dptable[0][col-1] and (s1[col-1] == s3[col-1])

for row in range(1, len(dptable)):
    dptable[row][0] = dptable[row-1][0] and ( dptable[row-1][0] and s2[row-1] == s3[row-1])

for row in range(1,len(dptable)):
    for col in range(1, len(dptable[0])):

        dptable[row][col] = ( dptable[row-1][col] and ( s2[row-1] == s3[row+col-1] )) or ( dptable[row][col-1]  and ( s1[col-1] == s3[row+col-1] )) 

for item in dptable:
    print(item)
print(dptable[-1][-1])


# return dptable[-1][-1]

# dptable = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]

# dptable[0][0] = True

# for col in range(1, len(dptable[0])):
#     dptable[0][col] = dptable[0][col-1] and (s1[col-1] == s3[col-1])

# for row in range(1, len(dptable)):
#     dptable[row][0] = dptable[row-1][0] and ( dptable[row-1][0] and s2[row-1] == s3[row-1])

# for row in range(1,len(dptable)):
#     for col in range(1, len(dptable[0])):
#         dptable[row][col] = (dptable[row-1][col] and (s2[row-1] == s3[row+col-1])) or (dptable[row][col-1] and (s1[col-1] == s3[row+col-1]))


        # dptable[row][col] = ( dptable[row-1][col] and ( s1[row-1] == s3[row+col-1] )) or ( dptable[row][col-1] and ( s2[col-1] == s3[row+col-1] )) 
        # or (dptable[row-1[col]] and s1[col-1] == s3[col+row-1])
        # (dptable[row-1][col] and (s1[col-1] == s3[row+col-1])) or (dptable[row][col-1] and (s2[row-1] == s3[row+col-1]))

