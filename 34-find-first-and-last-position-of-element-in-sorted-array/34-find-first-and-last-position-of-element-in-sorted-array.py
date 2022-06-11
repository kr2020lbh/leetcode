class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        return [self.func(nums,target,1),self.func(nums,target,0)]
    def func(self,nums,target,flag):
        ret = -1
        l,r = 0,len(nums)-1
        while l<=r:
            c = (l+r)//2
            if nums[c] == target:
                ret = c
            if flag:
                if nums[c] >= target:
                    r = c-1
                else:
                    l = c+1
            else:
                if nums[c] > target:
                    r = c-1
                else:
                    l = c+1
        return ret