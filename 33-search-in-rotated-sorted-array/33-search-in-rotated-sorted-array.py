class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            ret = nums.index(target)
        except ValueError:
            ret = -1
        return ret