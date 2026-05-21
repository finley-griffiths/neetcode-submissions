class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] < numbers[r]:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            r -= 1
            if numbers[l] == numbers[r]:
                r = len(numbers) - 1
                l += 1