class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.func(len(nums),0,0,[],nums,result)
        return result
    
    def func(self,n,cnt,bits,m_list,nums,result):
        if n == cnt:
            tmp = []
            for i in range(n):
                tmp.append(nums[m_list[i]])
            result.append(tmp)
            return
        for i in range(n):
            if not ((1 << i) & bits):
                self.func(n,cnt+1,(1 << i) | bits,m_list + [i],nums,result)