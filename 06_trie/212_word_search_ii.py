from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # define a trie and add words in the trie
        root = TrieNode()
        for word in words: 
            root.add_word(word)
        
        # run dfs to search word stored in the trie
        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()
        
        # define dfs function
        def dfs(row, col, curr_node, word_history):
            # define the base case to exit dfs function
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visit or
                board[row][col] not in curr_node.children
            ):
                return
            
            # go deeper by 1 step
            curr_node = curr_node.children[board[row][col]]
            word_history += board[row][col]
            visit.add((row, col))
            
            # search is completed
            if curr_node.is_end:
                result.add(word_history)
            
            # run dfs in 4 direction: up, down, left, right
            dfs(row + 1, col, curr_node, word_history)      # down
            dfs(row - 1, col, curr_node, word_history)      # up
            dfs(row, col + 1, curr_node, word_history)      # right
            dfs(row, col - 1, curr_node, word_history)      # left
            
            # take 1 step back
            visit.remove((row, col))
        
        # visit each element in the board and run dfs
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        
        return list(result)

def main():
    sol = Solution()
    
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
        ] 
    words = ["oath", "pea", "eat", "rain"]
    print(sol.findWords(board, words))
    
    board = [
        ["a","b"],
        ["c","d"]
        ]
    words = ["abcb"]
    print(sol.findWords(board, words))

if __name__ == "__main__":
    main()