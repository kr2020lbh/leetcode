from itertools import permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i] :
                tmpIdx = i-1
                for j in range(i,len(nums)):
                    if nums[i-1] < nums[j]:
                        tmpIdx = j
                nums[i-1],nums[tmpIdx] = nums[tmpIdx],nums[i-1]
                sIdx,eIdx = i,len(nums)
                if sIdx < eIdx:
                    nums[sIdx:eIdx] = nums[sIdx:eIdx][::-1]
                break
        else:
            nums.sort()
                        
                        
                               
                
        
    # 1 2 3 4 
    # 1 2 4 3
    # 1 3 2 4
    # 1 3 4 2
    # 1 4 2 3
    # 1 4 3 2
    # 2 1 3 4 
    