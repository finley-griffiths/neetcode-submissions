class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            k = (l + r) // 2
            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p / k)
            if eat_time <= h:
                result = k
                r = k-1
            else:
                l = k+1
        return result