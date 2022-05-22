from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numString = [
            [],
            [],
            ["a","b","c"],
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"]
        ]
        digitsIntType = list(map(int,digits))
        result = []
        depthLimit = len(digitsIntType)
        if depthLimit:
            self.dfs(result,0,depthLimit,numString,digitsIntType,[])
        return result
    
    
    def dfs(self,result,depth,depthLimit,numString,digits,indexes):
        if depth == depthLimit:
            tmp = ""
            for i in range(len(digits)):
                tmp += numString[digits[i]][indexes[i]]
            result.append(tmp)
            return
        
        for j in range(len(numString[digits[depth]])):
            self.dfs(result,depth+1,depthLimit,numString,digits,indexes + [j])
        
        