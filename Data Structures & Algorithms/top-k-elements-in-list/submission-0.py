class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        s = sorted(d.items(), key=lambda x: x[1])
        s = ([item[0] for item in s])[::-1]
        return s[:k]