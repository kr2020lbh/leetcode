class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        retList = []
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if num == val:
                nums.pop(i)
            else:
                ret += 1
        return ret
            
        