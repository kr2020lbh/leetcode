class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        tmp = [["." for _ in range(n)] for _ in range(n)]
        self.func(0,n,tmp,answer)
        return answer
    
    def func(self,row,n,tmp,answer):
        if row == n:
            ans = [''.join(t) for t in tmp]
            answer.append(ans)
            return
        for c in range(n):
            if self.check(row,c,tmp,n):
                tmp[row][c] = "Q"
                self.func(row+1,n,tmp,answer)
                tmp[row][c] = "."
    
    def check(self,r,c,checkList,n):
        for i in range(1,n):
            if 0<= (r-i) and checkList[r-i][c] == "Q":
                return False
        for i in range(1,n):
            if 0<= (c-i) and 0<= (r-i) and checkList[r-i][c-i] == "Q":
                return False
        for i in range(1,n):
            if (c+i) < n and 0<= (r-i) and checkList[r-i][c+i] == "Q":
                return False
        return True
            