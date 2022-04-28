class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sets = []
        for s in strs:
            new_set = set()
            for i in range(len(s)):
                new_set.add(s[:i+1])
            sets.append(new_set)
        u = set.intersection(*sets)
        result = sorted(u, key=lambda x:len(x))
        return result[-1] if result else ""
        
           