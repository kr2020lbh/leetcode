class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = [0]*201
        cnt = 0
        for num in nums:
            if newNums[num+100] == 0:
                newNums[num+100] = 1
                cnt += 1
        
        idx = 0
        tmp = cnt
        for i in range(len(newNums)):
            if newNums[i]:
                nums[idx] = i-100
                idx += 1
                tmp -= 1
            if tmp == 0:
                return cnt

                