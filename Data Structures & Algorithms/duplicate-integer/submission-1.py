class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = num
        if len(seen.keys()) != len(nums):
                return True
        return False