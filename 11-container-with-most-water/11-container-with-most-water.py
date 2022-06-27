class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        l_max,r_max = 0,0
        l_max_idx,r_max_idx = l,r
        ans = 0
        while l<r:
            if height[l] < height[r]:
                if l_max < height[l]:
                    ans = max(ans,max((l-l_max_idx)*l_max, (r-l)*height[l]))
                    l_max = height[l]
                    l_max_idx = l
                l += 1
            else:
                if r_max < height[r]:
                    ans = max(ans,max((r_max_idx-r)*r_max, (r-l)*height[r]))
                    r_max = height[r]
                    r_max_idx = r
                r -= 1
        return ans
            
            