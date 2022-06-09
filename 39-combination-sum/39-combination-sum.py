class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        for i in range(len(candidates)):
            self.dfs(i,[candidates[i]],candidates,target,answer)
        return answer
    
    def dfs(self,startIdx,curList,candidates,target,answer):
        if sum(curList) == target:
            answer.append(curList[::])
            return
        for i in range(startIdx,len(candidates)):
            if sum(curList) + candidates[i] <= target:
                curList.append(candidates[i])
                self.dfs(i,curList,candidates,target,answer)
                curList.pop()