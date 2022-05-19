s = "hit"
e = "cog"

wordlist = ["hot","dot","dog","lot","log"]
wordlist.append(e)
adjlist = {}

def get_val(word):
    print(word)
    result = []
    for j in range(len(word)):
        new_word = word[:j] + "*"+ word[j+1:]
        result.append(new_word)
    return new_word
    

for i in wordlist:

    for j in range(len(i)):
        new_word = i[:j] + "*"+i[j+1:]
        if new_word not in adjlist:
            adjlist[new_word] = [i]
        else:
            adjlist[new_word].append(i)


visited = []
visited.append(s)
count = [0]

def helper(node):
    print('helper called')
    visited.append(node)
    count[0] += 1

    for nbr in adjlist[word]:
        if nbr == e:
            return 
        
    for nbr in get_val(adjlist[word]):
        if nbr not in visited:
            visited.append(nbr)
            helper(nbr)


print(adjlist)
for i in range(len(s)):
    print(f"This is {i}")
    word = s[:i] + "*" + s[i+1:]
    print(word)
    if word not in adjlist:
        continue
    print("i")
    helper(word)

print(count)


