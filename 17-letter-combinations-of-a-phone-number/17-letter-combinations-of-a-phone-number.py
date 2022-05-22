from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.solution2(digits)
        
        
    def solution2(self,digits):
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
        digits = list(map(int,digits[::-1]))
        if not digits:
            return []
        tmp = numString[digits.pop()][::]
        while digits:
            ttmp = []
            for letter in numString[digits.pop()]:
                for t in tmp:
                    ttmp.append(t + letter)
            tmp = ttmp
        return tmp
        
    def solution1(self,digits):
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
        
        