class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = dict()
        for s in strs:
            k = ''.join(sorted(s))
            if strDict.get(k):
                strDict[k].append(s)
            else:
                strDict[k] = [s]
                
        ret = []
        for k,v in strDict.items():
            ret.append(v)
        return ret
            