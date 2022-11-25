start = "RX XL RX RXL"
end = "XR LX XR RLX"

word = "LRXRXL XXRRLX"
word2 = "LRXRXL XXRRLX"

intial = 0
curr = 1


start_whole_words = start[:intial] + start[curr+1:]
end_whole_words = end[:intial] + end[curr+1:]


print(start_whole_words, end_whole_words)
print(start_whole_words == end_whole_words)


 