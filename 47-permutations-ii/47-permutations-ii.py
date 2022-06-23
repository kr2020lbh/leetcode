class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        self.func(nums,0,[],ret)
        return [list(r) for r in ret]
    
    def func(self,nums,bit,tmp,ret):
        if bit == 2**len(nums)-1:
            ret.add(tuple(tmp))
            return
        for i in range(len(nums)):
            if not((1 << i) & bit):
                self.func(nums,bit | (1<<i),tmp + [nums[i]], ret)
                