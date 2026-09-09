class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums = sorted(nums)
        for i in range(len(nums)):
            c = -nums[i]
            j, k = i + 1, len(nums) - 1
            if i == 0 or nums[i] != nums[i-1]:
                while j < k:
                    s = nums[j] + nums[k]
                    if s < c:
                        j += 1
                    elif c < s:
                        k -= 1
                    elif s == c:
                        r.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    else:
                        break
        return r