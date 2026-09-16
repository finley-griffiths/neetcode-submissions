class Solution:
    def trap(self, height: List[int]) -> int:
        # set left pointer to left most, right pointer to right most
        # while they're not equal, move the lower of the two inwards
        # if it is a new max, record it
        # otherwise calculate the amount of water it holds
        l = 0
        r = len(height) - 1
        ml = height[l]
        mr = height[r]
        tw = 0
        while l != r:
            # move right
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