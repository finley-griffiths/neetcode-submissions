class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(set(nums))
        cc = 1
        hc = 1
        for num in nums:
            if num-1 in nums:
                cc += 1
                if cc > hc:
                    hc = cc
            else:
                cc = 1
        return hc