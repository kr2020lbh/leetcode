class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tmpRet = set()
        ret = []
        self.func(nums,0,[],tmpRet,ret)
        return ret
    
    def func(self,nums,bit,tmp,tmpRet,ret):
        if bit == 2**len(nums)-1:
            if not (tuple(tmp) in tmpRet):
                tmpRet.add(tuple(tmp))
                ret.append(tmp)
            return
        for i in range(len(nums)):
            if not((1 << i) & bit):
                self.func(nums,bit | (1<<i),tmp + [nums[i]], tmpRet, ret)
                