class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prev = 1
        for i in range(len(nums)):
            output.append(prev)
            prev = nums[i] * prev
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prev
            prev = nums[i] * prev
        return output