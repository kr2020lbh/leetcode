from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        mDict = defaultdict(int)
        result = []
        resultSet = set()
        for num in nums:
            mDict[num] += 1
        for i in range(n):
            a = nums[i]
            mDict[a] -= 1
            for j in range(i+1,n):
                b = nums[j]
                mDict[b] -= 1
                for k in range(j+1,n):
                    c = nums[k]
                    mDict[c] -= 1
                    d = target - (a+b+c)
                    if mDict[d]:
                        sortedTuple = tuple(sorted([a,b,c,d]))
                        if not (sortedTuple in resultSet):
                            resultSet.add(sortedTuple)
                            result.append([a,b,c,d])
                    
                    mDict[c] += 1
                mDict[b] += 1
            mDict[a] += 1
        return result