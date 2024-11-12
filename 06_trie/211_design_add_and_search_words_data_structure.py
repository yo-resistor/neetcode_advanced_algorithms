class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_word = True

    def search(self, word: str) -> bool:
        
        def search_helper(node: TrieNode, idx: int) -> bool:
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    for char_tree in node.children:
                        if search_helper(node.children[char_tree], i + 1):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
                
            return node.end_word
        
        return search_helper(self.root, 0)

        # def search_helper(node: TrieNode, word: str) -> bool:
        #     for char in word:
        #         print(f"character: {char}, word: {word}")
        #         print(f"end with? {node.end_word}")
        #         if char == '.':
        #             for char_tree in node.children:
        #                 if search_helper(node.children[char_tree], word[1:]):
        #                     return True
        #             return False
        #         else: 
        #             if char not in node.children:
        #                 return False
        #             node = node.children[char]
        #     return node.end_word
            
        # return search_helper(self.root, word)
            
def main():
    word_dict = WordDictionary()
    
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(word_dict.search("pad"))
    print(word_dict.search("bad"))
    print(word_dict.search(".ad"))
    print(word_dict.search("b.."))

if __name__ == "__main__":
    main()