class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        gList = []
        self.dfs([],candidates,0,0,target,gList)
        return gList
    
    
    def dfs(self,lList,candidates,curIdx,curSum,target,gList):
        if target < curSum:
            return
        
        if target == curSum:
            gList.append(lList[::])
            return
        
        for i in range(curIdx,len(candidates)):
            if curIdx < i and candidates[i] == candidates[i-1]:
                continue
            c = candidates[i]
            lList.append(c)
            self.dfs(lList,candidates,i+1,curSum+c,target,gList)
            lList.pop()