class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

def main():
    trie = Trie()
    
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    
    trie = Trie()
    
    trie.insert("bad")
    trie.insert("dad")
    trie.insert("pad")
    print(trie.search("bad"))
    print(trie.search("dad"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))

if __name__ == "__main__":
    main()