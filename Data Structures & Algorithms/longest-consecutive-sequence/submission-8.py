class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        hc = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cc = 1
                while num + 1 in nums_set:
                    num += 1
                    cc += 1
                hc = max(cc, hc)
        return hc