class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketSet = dict()
        bracketSet["("] = ")"
        bracketSet["["] = "]"
        bracketSet["{"] = "}"
        
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                lastBracket = stack.pop()
                if bracketSet[lastBracket] != bracket:
                    return False
        if stack:
            return False
        return True
                
            
        