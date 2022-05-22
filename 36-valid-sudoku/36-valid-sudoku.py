class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                ele = board[i][j]
                if ele != '.' and (ele in row):
                    return False
                else:
                    row.add(ele)
                    
        for j in range(len(board[0])):
            col = set()
            for i in range(len(board)):
                ele = board[i][j]
                if ele != '.' and (ele in col):
                    return False
                else:
                    col.add(ele)
                    
        for i in range(3):
            for j in range(3):
                r,c = i*3,j*3
                block = set()
                for _i in range(3):
                    for _j in range(3):
                        ele = board[r+_i][c+_j]
                        
                        if ele != '.' and (ele in block):
                            return False
                        else:
                            block.add(ele)
        return True
            
        
                
                