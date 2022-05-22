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
                    
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = set()
                print(i,j)
                for _i in range(3):
                    for _j in range(3):
                        ele = board[i+_i][j+_j]
                        if ele != '.' and (ele in square):
                            return False
                        else:
                            square.add(ele)
        return True
            
        
                
                