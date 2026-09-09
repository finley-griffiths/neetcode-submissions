class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums = sorted(nums)
        for i in range(len(nums)):
            c = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if (nums[j] + nums[k]) < c:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif c < (nums[j] + nums[k]):
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif (nums[j] + nums[k]) == c:
                    if [nums[i], nums[j], nums[k]] not in r:
                        r.append([nums[i], nums[j], nums[k]])
                    j += 1
                else:
                    break
        return r