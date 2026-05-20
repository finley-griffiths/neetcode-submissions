class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for j, row in enumerate(board):
            row_set = set()
            s_column = j // 3
            for i, num in enumerate(row):
                s_row = i // 3
                if num != '.':
                    # Columns check
                    if num in columns[i]:
                        return False
                    columns[i].add(num)
                    # Row check
                    if num in row_set:
                        return False
                    row_set.add(num)
                    # Squares check
                    square_index = s_row * 3 + s_column
                    if num in squares[square_index]:
                        return False
                    squares[square_index].add(num)
        return True

