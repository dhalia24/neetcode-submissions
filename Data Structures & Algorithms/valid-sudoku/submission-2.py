class Solution:
    def isValidRow(self, board: List[List[str]]) -> bool:
        j = 0 
        while j < 9:
            lst = []
            for i in range(0,9):
                if board[i][j] != ".":
                    lst.append(board[i][j])
            my_set = set(lst)
            if len(lst) != len(my_set):
                return False
            j += 1
        return True

    def isValidColumn(self, board: List[List[str]]) -> bool:
        i = 0
        while i < 9:
            lst = []
            for j in range(0,9):
                if board[i][j] != ".":
                    lst.append(board[i][j])
            my_set = set(lst)
            if len(lst) != len(my_set):
                return False
            i += 1
        return True


    def isValidBlock(self, board: List[List[str]]) -> bool:
        submatrices = []
        #extract the blocks         
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                # Slice rows, then slice columns from those rows
                block = [row[c:c+3] for row in board[r:r+3]]
                submatrices.append(block)
        
        for block in submatrices:  
            cells = []    
            for row in block:          
                for value in row: 
                    if value != ".":
                        cells.append(value)
            my_set = set(cells)
            if (len(my_set) != len(cells)):
                return False
        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidColumn(board) and self.isValidBlock(board)
        