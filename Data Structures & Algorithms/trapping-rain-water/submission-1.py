class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ml = height[l]
        mr = height[r]
        tw = 0
        while l != r:
            if height[l] > height[r]:
                r -= 1
                if height[r] > mr:
                    mr = height[r]
                else:
                    tw += min(ml, mr) - height[r]
            else:
                l += 1
                if height[l] > ml:
                    ml = height[l]
                else:
                    tw += min(ml, mr) - height[l]
        return tw