from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                self.prefix[row][col] += (
                    matrix[row][col]
                    + (self.prefix[row - 1][col] if row > 0 else 0)
                    + (self.prefix[row][col - 1] if col > 0 else 0)
                    - (self.prefix[row - 1][col - 1] if row > 0 and col > 0 else 0)
                )
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        res += (
            self.prefix[row2][col2]
            - (self.prefix[row1 - 1][col2] if row1 > 0 else 0)
            - (self.prefix[row2][col1 - 1] if col1 > 0 else 0)
            + (self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
        )
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def main():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    num_matrix = NumMatrix(matrix)
    print(num_matrix.sumRegion(2, 1, 4, 3))
    print(num_matrix.sumRegion(1, 1, 2, 2))
    print(num_matrix.sumRegion(1, 2, 2, 4))

if __name__ == "__main__":
    main()