class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        v = [[0]*n for _ in range(n)]
        for r in range(n//2+1):
            for c in range(n//2+1):
                if not v[r][c]:
                    self.points(r,c,n-1,matrix,v)
                
    def points(self,r,c,n,matrix,v):
        r1,c1 = r,c
        r2,c2 = c1,n-r1
        r3,c3 = c2,n-r2
        r4,c4 = c3,n-r3
        v[r1][c1] = 1
        v[r2][c2] = 1
        v[r3][c3] = 1
        v[r4][c4] = 1
        matrix[r1][c1],matrix[r2][c2],matrix[r3][c3],matrix[r4][c4] = matrix[r4][c4],matrix[r1][c1],matrix[r2][c2],matrix[r3][c3]
    