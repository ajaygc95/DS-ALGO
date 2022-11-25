class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.word_end = False


    def insert(self, word):
        curr = self

        for character in word:
            if character not in curr.children:
                curr.children[character] = Trie()
            curr = curr.children[character]

        curr.word_end = True

    def delete(self, word):
        curr = self
        stack = []
        for character in word:
            if character not in curr.children:
                print("There is no such word {}".format(word))
                return False
            stack.append(curr)
            curr = curr.children[character]
        
        if not curr.word_end:
            return False

        curr.word_end = False
        for char in word[::-1]:

            if len(curr.children) == 0 and not curr.word_end:
                curr = stack.pop()
                del curr.children[char]


    def view(self,trie):
        curr = trie

        for character in curr.children:
            print(character, end="-->")
            self.view(curr.children[character])

        print(end=" ")
        
trie = Trie()
trie.insert("APPLE")
trie.insert("BANANA")
trie.insert("APPLD")
trie.view(trie)
trie.delete("APPLD")
print()
trie.view(trie)