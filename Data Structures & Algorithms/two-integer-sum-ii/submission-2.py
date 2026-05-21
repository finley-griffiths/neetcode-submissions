class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            c = target - numbers[i]
            for j in range(len(numbers[i:])):
                if numbers[j+i] == c:
                    return [i+1, i+j+1]