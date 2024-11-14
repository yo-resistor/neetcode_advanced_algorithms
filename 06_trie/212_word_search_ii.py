from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        result = []
        
        def search(idx, row, col, board, check, word):
            # if the element is not inside the board
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS
            ):
                return False
            
            # if the idx is out of word
            # we succeeded
            if idx >= len(word) or idx < 0:
                return True
            
            print(f"interest: {word[idx]} / on board: {board[row][col]}")
            # if we find the element in the board
            # and it was not explored before
            if word[idx] == board[row][col] and check[row][col] == 0:
                print("found")
                check[row][col] = 1
                return (
                    search(idx + 1, row + 1, col, board, check, word) or
                    search(idx + 1, row - 1, col, board, check, word) or
                    search(idx + 1, row, col + 1, board, check, word) or
                    search(idx + 1, row, col - 1, board, check, word)
                )
        
        for word in words:
            print(f"target: [{word}]")
            word_idx = 0
            for row in range(ROWS):
                if word[word_idx] in board[row]:
                    for col in range(COLS):
                        if word[word_idx] == board[row][col]:
                            board_check = [[0 for j in range(COLS)] for i in range(ROWS)]
                            if search(word_idx, row, col, board, board_check, word):
                                result.append(word)
        
        return result

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