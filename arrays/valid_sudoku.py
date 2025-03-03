'''

Given: 9x9 list[list[str]]
Return: true if valid board else false

* Board can be valid even if neither full nor solvable

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.validateRows(board) and 
            self.validateColumns(board) and 
            self.validateGrids(board)
        )

    def validateRows(self, board: List[List[str]]):
        for row in board:
            mem = dict()
            for num in row:
                if num == ".": continue
                mem[num] = mem.get(num, 0) + 1
                if mem[num] > 1: return False # duplicate found
        return True

    # we want j to continue updating while we lock in i -> arr[j][i]
    def validateColumns(self, board: List[List[str]]):
        for i in range(len(board)):
            mem = defaultdict(int)
            for j in range(len(board[i])):
                if board[j][i] == ".": continue
                mem[board[j][i]] += 1
                if mem[board[j][i]] > 1: return False #duplicate found
        return True

    # increment pointer
    # check 3x3
    def validateGrids(self, board: List[List[str]]):
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                mem = defaultdict(int)
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == ".": continue
                        mem[board[k][l]] += 1
                        if mem[board[k][l]] > 1: return False # duplicate found
        return True











