from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numDict = defaultdict(int)
        n = len(nums)
        newNums = []
        result = []
        resultSet = set()
        for i in range(n):
            if numDict[nums[i]] == 3:
                continue
            numDict[nums[i]] += 1
            newNums.append(nums[i])
        n = len(newNums)
        for i in range(n):
            a = newNums[i]
            numDict[a] -= 1
            for j in range(i+1,n):
                b = newNums[j]
                numDict[b] -= 1
                c = - (a+b)
                tmp = sorted([a,b,c])
                if numDict[c] and not(tuple(tmp) in resultSet):
                    resultSet.add(tuple(tmp))
                    result.append(tmp)
                numDict[b] += 1
            numDict[a] += 1
        return result
                    