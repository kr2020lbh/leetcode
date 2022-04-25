class Solution(object):
    def twoSum(self, nums, target):
        enum_nums = sorted(list(enumerate(nums)),key=lambda x:x[1])
        l,r = 0,len(nums)-1
        while 1:
            l_n,r_n = enum_nums[l][1],enum_nums[r][1]
            if l_n + r_n < target:
                l += 1
            elif l_n + r_n > target:
                r -= 1
            else:
                return [enum_nums[l][0],enum_nums[r][0]]
            
        