class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        for i in range(len(candidates)):
            self.dfs(i,[candidates[i]],candidates,target-candidates[i],answer)
        return answer
    
    def dfs(self,startIdx,curList,candidates,target,answer):
        if target < 0:
            return 
        
        if target == 0:
            answer.append(curList[::])
            return
        
        for i in range(startIdx,len(candidates)):
            self.dfs(i,curList  + [candidates[i]],candidates,target-candidates[i],answer)
