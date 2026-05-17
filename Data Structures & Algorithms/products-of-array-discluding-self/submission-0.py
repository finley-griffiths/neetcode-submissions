class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prfix = []
        psfix = []
        output = []
        prev = 1
        for i in range(len(nums)):
            prfix.append(prev)
            prev = nums[i] * prev
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            psfix.append(prev)
            prev = nums[i] * prev
        psfix = list(reversed(psfix))
        for i in range(len(nums)):
            output.append(psfix[i] * prfix[i])
        return output