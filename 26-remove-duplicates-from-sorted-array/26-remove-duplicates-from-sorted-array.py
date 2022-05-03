class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setNums = sorted(list(set(nums)))
        n = len(setNums)
        for i in range(len(nums)):
            if i < n:
                nums[i] = setNums[i]
            else:
                nums[i] = "_"
        return len(setNums)