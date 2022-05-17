class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if nums[-1] < target:
            return len(nums)
        if len(nums) == 2:
            return 1
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            tmp = nums[mid]
            if tmp == target:
                return mid

                
            if tmp < target:
                l = mid + 1
            else:
                r = mid - 1
        print(l,r,mid)
        return l