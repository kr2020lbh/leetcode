class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.func("",n,n,[])
    
    def func(self,p,left,right,result):
        if left: self.func(p+'(',left-1,right,result)
        if left<right: self.func(p+')',left,right-1,result)
        if not right: result.append(p)
        return result
        
                
        