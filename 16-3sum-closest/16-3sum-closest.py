class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if abs(target - cur) < abs(target - ret):
                    ret = cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return ret
        return ret