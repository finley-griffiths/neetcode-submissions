class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, m in enumerate(matrix):
            if target >= m[0] or target <= m[-1]:
                l, r = 0, len(m)-1
                while l <= r:
                    mid = (l + r) // 2
                    if m[mid] == target:
                        return True
                    elif m[mid] <= target:
                        l = mid + 1
                    elif m[mid] >= target:
                        r = mid - 1
        return False