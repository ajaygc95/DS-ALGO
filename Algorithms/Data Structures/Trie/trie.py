class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = {}
        self.is_word = False
        self.parent = None
    
    def insert(self,word):
        curr = self
        for character in word:
            if character not in curr.children:
                curr.children[character] = TrieNode(character)
                curr.children[character].parent = curr

            curr = curr.children[character]
        curr.is_word = True

    def view(self, word):
        curr = self
        for character in word:
            print(curr.parent, curr.char)
            if character not in curr.children:
                return False
            curr = curr.children[character]
        print(curr.parent, curr.char)
        print(f"All Printed {word}")

    def delete(self, word):
        curr = self
        for character in word:
            if character not in curr.children:
                return False
            curr = curr.children[character]

        curr.is_word = False
        while curr.parent is not None and not curr.is_word and not curr.children:
            child = curr
            curr = curr.parent
            del curr.children[child.char]

trie = TrieNode()
trie.insert("apple")
trie.insert("appliphone")
trie.view('appliphone')
trie.delete('appliphone')
trie.view('apple')