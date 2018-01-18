class TrieNode:
    def __init__(self, a):
        self.val = a
        self.dict = {}
        self.list = []

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("a")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        travel = self.root
        for i in word:
            if i in travel.dict:
                travel = travel.dict.get(i)
            else:
                travel.dict[i] = TrieNode(i)
                travel = travel.dict.get(i)
        travel.list.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        travel = self.root
        for i in word:
            if i in travel.dict:
                travel = travel.dict.get(i)
            else:
                return False
        return word in travel.list

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        travel = self.root
        for i in prefix:
            if i in travel.dict:
                travel = travel.dict.get(i)
            else:
                return False
        return True

obj = Trie()
obj.insert("abc")
param_2 = obj.search("ab")
param_3 = obj.startsWith("abc")
print(param_2, param_3)